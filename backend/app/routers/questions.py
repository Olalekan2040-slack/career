from fastapi import APIRouter

from .. import schemas
from ..data.questions_v3 import (
    FORCED_CHOICE_QUESTIONS,
    LIKERT_QUESTIONS,
    RANKING_QUESTIONS,
    SCENARIO_QUESTIONS,
    SITUATIONAL_QUESTIONS,
)

router = APIRouter(prefix="/api/questions", tags=["questions"])


def _likert_out(question: dict) -> dict:
    return {"id": question["id"], "text": question["text"]}


def _choice_out(question: dict) -> dict:
    return {
        "id": question["id"],
        "text": question["text"],
        "options": [{"key": key, "text": opt["text"]} for key, opt in question["options"].items()],
    }


def _ranking_out(question: dict) -> dict:
    return {
        "id": question["id"],
        "text": question["text"],
        "items": [{"key": key, "text": item["text"]} for key, item in question["items"].items()],
    }


@router.get("", response_model=schemas.QuestionSetOut)
def get_questions():
    return {
        "likert": [_likert_out(q) for q in LIKERT_QUESTIONS],
        "forced_choice": [_choice_out(q) for q in FORCED_CHOICE_QUESTIONS],
        "scenario": [_choice_out(q) for q in SCENARIO_QUESTIONS],
        "situational": [_choice_out(q) for q in SITUATIONAL_QUESTIONS],
        "ranking": [_ranking_out(q) for q in RANKING_QUESTIONS],
    }
