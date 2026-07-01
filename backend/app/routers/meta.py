from fastapi import APIRouter

from ..data.careers import CAREERS
from ..data.competencies import COMPETENCIES
from ..data.questions_v3 import (
    FORCED_CHOICE_QUESTIONS,
    LIKERT_QUESTIONS,
    RANKING_QUESTIONS,
    SCENARIO_QUESTIONS,
    SITUATIONAL_QUESTIONS,
)

router = APIRouter(prefix="/api/meta", tags=["meta"])


@router.get("")
def get_meta():
    return {
        "career_count": len(CAREERS),
        "competency_count": len(COMPETENCIES),
        "competencies": [{"code": code, "name": name} for code, name in COMPETENCIES.items()],
        "careers": sorted(career["name"] for career in CAREERS.values()),
        "question_counts": {
            "likert": len(LIKERT_QUESTIONS),
            "forced_choice": len(FORCED_CHOICE_QUESTIONS),
            "scenario": len(SCENARIO_QUESTIONS),
            "situational": len(SITUATIONAL_QUESTIONS),
            "ranking": len(RANKING_QUESTIONS),
            "total": (
                len(LIKERT_QUESTIONS)
                + len(FORCED_CHOICE_QUESTIONS)
                + len(SCENARIO_QUESTIONS)
                + len(SITUATIONAL_QUESTIONS)
                + len(RANKING_QUESTIONS)
            ),
        },
    }
