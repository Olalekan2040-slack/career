from . import models
from .data.careers import get_career

CLOSE_CALL_MESSAGE = (
    "You scored closely across multiple paths — this means you have versatile strengths. "
    "A consultation with Sharafdeen will help you make the best choice."
)


def build_result_out(result: models.Result) -> dict:
    """Everyone gets their full set of recommendations — there is no
    login-gated tiering anymore, just a name+email lead capture."""
    recommendations = [
        {
            "rank": i + 1,
            "score": item["score"],
            "reason": item["reason"],
            "entry_note": item.get("entry_note"),
            "career": get_career(item["career_key"]),
        }
        for i, item in enumerate(result.recommendations)
    ]

    return {
        "id": result.id,
        "unlocked": True,
        "visible_count": len(recommendations),
        "close_call": result.close_call,
        "close_call_message": CLOSE_CALL_MESSAGE if result.close_call else None,
        "recommendations": recommendations,
        "created_at": result.created_at,
    }
