from . import models
from .data.careers import get_career

CLOSE_CALL_MESSAGE = (
    "You scored closely across multiple paths — this means you have versatile strengths. "
    "A consultation with Sharafdeen will help you make the best choice."
)


def build_result_out(result: models.Result, force_unlock: bool = False) -> dict:
    effective_unlocked = result.unlocked or force_unlock
    visible_count = 4 if effective_unlocked else 2

    visible = result.recommendations[:visible_count]
    recommendations = [
        {
            "rank": i + 1,
            "score": item["score"],
            "reason": item["reason"],
            "career": get_career(item["career_key"]),
        }
        for i, item in enumerate(visible)
    ]

    return {
        "id": result.id,
        "unlocked": effective_unlocked,
        "visible_count": visible_count,
        "close_call": result.close_call,
        "close_call_message": CLOSE_CALL_MESSAGE if result.close_call else None,
        "recommendations": recommendations,
        "created_at": result.created_at,
    }
