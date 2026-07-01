from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas
from ..auth import get_optional_user
from ..config import settings
from ..data.categories import get_category
from ..database import get_db
from ..email_service import render_free_tier_email, render_paid_tier_email, send_email
from ..result_builder import build_result_out
from ..scoring import compute_result

router = APIRouter(prefix="/api/submit", tags=["submit"])


@router.post("", response_model=schemas.ResultOut)
def submit_assessment(
    payload: schemas.SubmitRequest,
    db: Session = Depends(get_db),
    current_user: models.User | None = Depends(get_optional_user),
):
    lead = db.get(models.Lead, payload.lead_id)
    if lead is None:
        raise HTTPException(status_code=404, detail="Lead not found")

    # If the lead was created before the user logged in (or the token wasn't sent yet),
    # attach it to their account now so it shows up in their dashboard.
    if current_user is not None and lead.user_id is None:
        lead.user_id = current_user.id
        db.commit()

    response = models.AssessmentResponse(
        lead_id=lead.id,
        answers={
            "orientation": payload.orientation_answers,
            "deep_dive": payload.deep_dive_answers,
        },
    )
    db.add(response)
    db.flush()

    computed = compute_result(payload.orientation_answers, payload.deep_dive_answers)

    # Having an account replaces the $1 paywall — signed-in users get full detail immediately.
    has_account = current_user is not None and lead.user_id == current_user.id

    result = models.Result(
        response_id=response.id,
        primary_category=computed["primary_category"],
        secondary_category=computed["secondary_category"],
        scores=computed["scores"],
        track=computed["track"],
        close_call=computed["close_call"],
        unlocked=has_account,
    )
    db.add(result)
    db.commit()
    db.refresh(result)

    try:
        primary = get_category(result.primary_category)
        secondary = get_category(result.secondary_category)
        if has_account:
            html = render_paid_tier_email(lead.name, primary, secondary, settings.consultation_booking_url)
            send_email(lead.email, "Your full Digital Career roadmap — strengths & course outline", html)
            result.paid_email_sent = True
        else:
            result_url = f"{settings.frontend_url}/results/{result.id}"
            html = render_free_tier_email(lead.name, primary, result_url)
            send_email(lead.email, "Your Digital Career Assessment result is ready", html)
            result.free_email_sent = True
        db.commit()
    except Exception as exc:  # pragma: no cover - best-effort email delivery
        print(f"[submit] failed to send result email: {exc}")

    return build_result_out(result, force_unlock=has_account)
