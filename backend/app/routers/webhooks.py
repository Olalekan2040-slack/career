from fastapi import APIRouter, BackgroundTasks, Depends, Header, HTTPException, Request
from sqlalchemy.orm import Session

from .. import models
from ..config import settings
from ..database import SessionLocal, get_db
from ..email_service import render_recommendations_email, send_email
from ..payments import verify_paystack_signature, verify_stripe_webhook
from ..result_builder import build_result_out

router = APIRouter(prefix="/api/webhooks", tags=["webhooks"])


def _unlock_result_and_notify(result_id: str) -> None:
    """Runs in the background — Stripe/Paystack expect a fast webhook ack, and the
    SMTP round trip shouldn't hold that up (or the user's results page either)."""
    db = SessionLocal()
    try:
        result = db.get(models.Result, result_id)
        if result is None or result.unlocked:
            return

        result.unlocked = True
        db.commit()

        lead = result.response.lead
        result_out = build_result_out(result, force_unlock=True)
        result_url = f"{settings.frontend_url}/results/{result.id}"
        html = render_recommendations_email(
            lead.name, result_out["recommendations"], True, result_url, settings.consultation_booking_url
        )
        send_email(lead.email, "Your full Digital Career roadmap is unlocked 🔓", html)
        result.paid_email_sent = True
        db.commit()
    except Exception as exc:  # pragma: no cover - best-effort email delivery
        print(f"[webhooks] failed to unlock/notify: {exc}")
    finally:
        db.close()


@router.post("/stripe")
async def stripe_webhook(
    request: Request,
    background_tasks: BackgroundTasks,
    stripe_signature: str = Header(None, alias="stripe-signature"),
    db: Session = Depends(get_db),
):
    payload = await request.body()
    try:
        event = verify_stripe_webhook(payload, stripe_signature)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"Invalid Stripe webhook: {exc}")

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        result_id = session.get("metadata", {}).get("result_id")
        result = db.get(models.Result, result_id) if result_id else None
        if result is not None:
            payment = (
                db.query(models.Payment)
                .filter(models.Payment.result_id == result.id, models.Payment.provider == "stripe")
                .order_by(models.Payment.created_at.desc())
                .first()
            )
            if payment is not None:
                payment.status = "success"
                payment.provider_reference = session.get("id")
            db.commit()
            background_tasks.add_task(_unlock_result_and_notify, result.id)

    return {"received": True}


@router.post("/paystack")
async def paystack_webhook(
    request: Request,
    background_tasks: BackgroundTasks,
    x_paystack_signature: str = Header(None, alias="x-paystack-signature"),
    db: Session = Depends(get_db),
):
    payload = await request.body()
    if not verify_paystack_signature(payload, x_paystack_signature):
        raise HTTPException(status_code=400, detail="Invalid Paystack signature")

    event = await request.json()
    if event.get("event") == "charge.success":
        data = event["data"]
        reference = data.get("reference")
        payment = (
            db.query(models.Payment)
            .filter(models.Payment.provider_reference == reference, models.Payment.provider == "paystack")
            .first()
        )
        if payment is not None:
            payment.status = "success"
            db.commit()
            if payment.result_id:
                background_tasks.add_task(_unlock_result_and_notify, payment.result_id)

    return {"received": True}
