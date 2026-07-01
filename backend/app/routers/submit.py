from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas
from ..auth import get_optional_user
from ..config import settings
from ..database import SessionLocal, get_db
from ..email_service import render_recommendations_email, send_email
from ..result_builder import build_result_out
from ..scoring_v3 import ScoringError, compute_recommendations

router = APIRouter(prefix="/api/submit", tags=["submit"])

CLOSE_CALL_SCORE_SPREAD = 0.08


def _send_result_email_task(result_id: str, has_account: bool) -> None:
    """Runs after the HTTP response has already been sent — the SMTP round trip
    (TLS handshake + login + send) can take several seconds and must never block
    the user's "view results" navigation."""
    db = SessionLocal()
    try:
        result = db.get(models.Result, result_id)
        if result is None:
            return
        lead = result.response.lead

        result_out = build_result_out(result, force_unlock=has_account)
        result_url = f"{settings.frontend_url}/results/{result.id}"
        html = render_recommendations_email(
            lead.name, result_out["recommendations"], has_account, result_url, settings.consultation_booking_url
        )
        subject = (
            "Your full Digital Career roadmap — strengths & course outlines"
            if has_account
            else "Your Digital Career Assessment matches are ready"
        )
        send_email(lead.email, subject, html)

        if has_account:
            result.paid_email_sent = True
        else:
            result.free_email_sent = True
        db.commit()
    except Exception as exc:  # pragma: no cover - best-effort email delivery
        print(f"[submit] failed to send result email: {exc}")
    finally:
        db.close()


@router.post("", response_model=schemas.ResultOut)
def submit_assessment(
    payload: schemas.SubmitRequest,
    background_tasks: BackgroundTasks,
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

    answers = payload.answers.model_dump()

    response = models.AssessmentResponse(lead_id=lead.id, answers=answers)
    db.add(response)
    db.flush()

    try:
        recommendations = compute_recommendations(answers, count=4)
    except ScoringError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

    scores = [r["score"] for r in recommendations]
    close_call = (max(scores) - min(scores)) < CLOSE_CALL_SCORE_SPREAD if len(scores) > 1 else False

    has_account = current_user is not None and lead.user_id == current_user.id

    result = models.Result(
        response_id=response.id,
        recommendations=recommendations,
        close_call=close_call,
        unlocked=has_account,
    )
    db.add(result)
    db.commit()
    db.refresh(result)

    background_tasks.add_task(_send_result_email_task, result.id, has_account)

    return build_result_out(result, force_unlock=has_account)
