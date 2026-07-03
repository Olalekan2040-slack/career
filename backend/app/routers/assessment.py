from fastapi import APIRouter

from .. import schemas
from ..adaptive import select_next_question, should_stop
from ..data.intake import INTAKE_FIELDS
from ..question_serializers import serialize_question
from ..scoring_v3 import total_answered_count

router = APIRouter(prefix="/api/assessment", tags=["assessment"])


@router.get("/intake-schema", response_model=list[schemas.IntakeFieldOut])
def get_intake_schema():
    return INTAKE_FIELDS


@router.post("/next", response_model=schemas.NextQuestionResponse)
def get_next_question(payload: schemas.NextQuestionRequest):
    answers = payload.answers.model_dump()
    intake = payload.intake.model_dump()
    total_answered = total_answered_count(answers)

    if should_stop(answers, payload.elapsed_seconds):
        return {"done": True, "total_answered": total_answered, "next": None}

    result = select_next_question(intake, answers, set(payload.skipped_ids))
    if result is None:
        return {"done": True, "total_answered": total_answered, "next": None}

    return {
        "done": False,
        "total_answered": total_answered,
        "next": {"section": result["section"], "question": serialize_question(result["section"], result["question"])},
    }
