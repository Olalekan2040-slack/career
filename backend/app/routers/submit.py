from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas
from ..auth import get_current_user
from ..config import settings
from ..database import SessionLocal, get_db
from ..email_service import render_recommendations_email, send_email
from ..result_builder import build_result_out
from ..scoring_v3 import ScoringError, compute_recommendations

router = APIRouter(prefix="/api/submit", tags=["submit"])

CLOSE_CALL_SCORE_SPREAD = 0.08


def _send_result_email_task(result_id: str) -> None:
    """Runs after the HTTP response has already been sent — the SMTP round trip
    (TLS handshake + login + send) can take several seconds and must never block
    the user's "view results" navigation."""
    db = SessionLocal()
    try:
        result = db.get(models.Result, result_id)
        if result is None:
            return
        lead = result.response.lead

        result_out = build_result_out(result, force_unlock=True)
        result_url = f"{settings.frontend_url}/results/{result.id}"
        html = render_recommendations_email(
            lead.name, result_out["recommendations"], True, result_url, settings.consultation_booking_url
        )
        send_email(lead.email, "Your full Digital Career roadmap — strengths & course outlines", html)

        result.paid_email_sent = True
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
    current_user: models.User = Depends(get_current_user),
):
    lead = db.get(models.Lead, payload.lead_id)
    if lead is None:
        raise HTTPException(status_code=404, detail="Lead not found")

    if lead.user_id is None:
        lead.user_id = current_user.id
        db.commit()
    elif lead.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="This assessment session belongs to a different account")

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

    result = models.Result(
        response_id=response.id,
        recommendations=recommendations,
        close_call=close_call,
        unlocked=True,
    )
    db.add(result)
    db.commit()
    db.refresh(result)

    background_tasks.add_task(_send_result_email_task, result.id)

    return build_result_out(result, force_unlock=True)
