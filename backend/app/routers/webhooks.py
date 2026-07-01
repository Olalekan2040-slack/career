from fastapi import APIRouter, Depends, Header, HTTPException, Request
from sqlalchemy.orm import Session

from .. import models
from ..config import settings
from ..data.categories import get_category
from ..database import get_db
from ..email_service import render_paid_tier_email, send_email
from ..payments import verify_paystack_signature, verify_stripe_webhook

router = APIRouter(prefix="/api/webhooks", tags=["webhooks"])


def _unlock_result_and_notify(db: Session, result: models.Result) -> None:
    if result.unlocked:
        return

    result.unlocked = True
    db.commit()

    lead = result.response.lead
    primary = get_category(result.primary_category)
    secondary = get_category(result.secondary_category)

    try:
        html = render_paid_tier_email(lead.name, primary, secondary, settings.consultation_booking_url)
        send_email(lead.email, "Your full Digital Career roadmap is unlocked 🔓", html)
        result.paid_email_sent = True
        db.commit()
    except Exception as exc:  # pragma: no cover - best-effort email delivery
        print(f"[webhooks] failed to send paid-tier email: {exc}")


@router.post("/stripe")
async def stripe_webhook(
    request: Request,
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
            _unlock_result_and_notify(db, result)

    return {"received": True}


@router.post("/paystack")
async def paystack_webhook(
    request: Request,
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
            result = db.get(models.Result, payment.result_id)
            if result is not None:
                _unlock_result_and_notify(db, result)

    return {"received": True}
