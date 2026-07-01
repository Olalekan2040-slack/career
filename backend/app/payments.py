"""Stripe + Paystack checkout session creation and webhook signature verification.

Both providers are wired for test-mode keys by default (see .env.example).
Swapping to live keys at launch requires no code changes.
"""

import hashlib
import hmac

import requests
import stripe

from .config import settings

stripe.api_key = settings.stripe_secret_key

PAYSTACK_BASE_URL = "https://api.paystack.co"


def create_stripe_checkout_session(result_id: str, email: str) -> str:
    session = stripe.checkout.Session.create(
        mode="payment",
        payment_method_types=["card"],
        customer_email=email,
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {"name": "Digital Career Assessment — Full Unlock"},
                    "unit_amount": settings.stripe_price_usd_cents,
                },
                "quantity": 1,
            }
        ],
        metadata={"result_id": result_id},
        success_url=f"{settings.frontend_url}/results/{result_id}?payment=success",
        cancel_url=f"{settings.frontend_url}/results/{result_id}?payment=cancelled",
    )
    return session.url


def create_paystack_checkout_session(result_id: str, email: str) -> dict:
    response = requests.post(
        f"{PAYSTACK_BASE_URL}/transaction/initialize",
        headers={"Authorization": f"Bearer {settings.paystack_secret_key}"},
        json={
            "email": email,
            "amount": settings.paystack_amount_kobo,
            "currency": "NGN",
            "metadata": {"result_id": result_id},
            "callback_url": f"{settings.frontend_url}/results/{result_id}?payment=confirming",
        },
        timeout=15,
    )
    response.raise_for_status()
    data = response.json()["data"]
    return {"authorization_url": data["authorization_url"], "reference": data["reference"]}


def verify_stripe_webhook(payload: bytes, signature_header: str):
    return stripe.Webhook.construct_event(payload, signature_header, settings.stripe_webhook_secret)


def verify_paystack_signature(payload: bytes, signature_header: str) -> bool:
    expected = hmac.new(
        settings.paystack_secret_key.encode("utf-8"), payload, hashlib.sha512
    ).hexdigest()
    return hmac.compare_digest(expected, signature_header or "")


def verify_paystack_transaction(reference: str) -> dict:
    response = requests.get(
        f"{PAYSTACK_BASE_URL}/transaction/verify/{reference}",
        headers={"Authorization": f"Bearer {settings.paystack_secret_key}"},
        timeout=15,
    )
    response.raise_for_status()
    return response.json()
