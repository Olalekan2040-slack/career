from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas
from ..config import settings
from ..database import get_db
from ..payments import create_paystack_checkout_session, create_stripe_checkout_session

router = APIRouter(prefix="/api/checkout", tags=["checkout"])


def _get_result_and_lead(db: Session, result_id: str):
    result = db.get(models.Result, result_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Result not found")
    lead = result.response.lead
    return result, lead


@router.post("/stripe", response_model=schemas.CheckoutResponse)
def checkout_stripe(payload: schemas.CheckoutRequest, db: Session = Depends(get_db)):
    result, lead = _get_result_and_lead(db, payload.result_id)

    try:
        checkout_url = create_stripe_checkout_session(result.id, lead.email)
    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail="Stripe checkout is not available right now. Please check the Stripe API keys or try again shortly.",
        ) from exc

    payment = models.Payment(
        result_id=result.id,
        provider="stripe",
        amount=settings.stripe_price_usd_cents / 100,
        currency="USD",
        status="pending",
    )
    db.add(payment)
    db.commit()

    return {"checkout_url": checkout_url, "provider": "stripe"}


@router.post("/paystack", response_model=schemas.CheckoutResponse)
def checkout_paystack(payload: schemas.CheckoutRequest, db: Session = Depends(get_db)):
    result, lead = _get_result_and_lead(db, payload.result_id)

    try:
        session = create_paystack_checkout_session(result.id, lead.email)
    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail="Paystack checkout is not available right now. Please check the Paystack API keys or try again shortly.",
        ) from exc

    payment = models.Payment(
        result_id=result.id,
        provider="paystack",
        amount=settings.paystack_amount_kobo / 100,
        currency="NGN",
        status="pending",
        provider_reference=session["reference"],
    )
    db.add(payment)
    db.commit()

    return {"checkout_url": session["authorization_url"], "provider": "paystack"}
