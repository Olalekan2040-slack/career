from fastapi import APIRouter

from .. import schemas
from ..data.questions import ORIENTATION_QUESTIONS, TRACK_A_QUESTIONS, TRACK_B_QUESTIONS
from ..scoring import determine_track

router = APIRouter(prefix="/api/questions", tags=["questions"])


def _to_question_out(question: dict) -> dict:
    return {
        "id": question["id"],
        "text": question["text"],
        "options": [
            {"key": key, "text": option["text"]} for key, option in question["options"].items()
        ],
    }


@router.get("", response_model=schemas.QuestionSetOut)
def get_questions():
    return {
        "orientation": [_to_question_out(q) for q in ORIENTATION_QUESTIONS],
        "track_a_deep_dive": [_to_question_out(q) for q in TRACK_A_QUESTIONS],
        "track_b_deep_dive": [_to_question_out(q) for q in TRACK_B_QUESTIONS],
    }


@router.post("/route")
def route_track(orientation_answers: dict[str, str]):
    """Given completed orientation answers, returns which track's deep-dive to show next."""
    return {"track": determine_track(orientation_answers)}
