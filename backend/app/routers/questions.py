from fastapi import APIRouter

from .. import schemas
from ..data.questions_v3 import (
    FORCED_CHOICE_QUESTIONS,
    LIKERT_QUESTIONS,
    RANKING_QUESTIONS,
    SCENARIO_QUESTIONS,
    SITUATIONAL_QUESTIONS,
)
from ..question_serializers import serialize_question

router = APIRouter(prefix="/api/questions", tags=["questions"])


@router.get("", response_model=schemas.QuestionSetOut)
def get_questions():
    return {
        "likert": [serialize_question("likert", q) for q in LIKERT_QUESTIONS],
        "forced_choice": [serialize_question("forced_choice", q) for q in FORCED_CHOICE_QUESTIONS],
        "scenario": [serialize_question("scenario", q) for q in SCENARIO_QUESTIONS],
        "situational": [serialize_question("situational", q) for q in SITUATIONAL_QUESTIONS],
        "ranking": [serialize_question("ranking", q) for q in RANKING_QUESTIONS],
    }
