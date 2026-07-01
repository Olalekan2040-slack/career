from . import models
from .data.categories import get_category


def build_result_out(result: models.Result, force_unlock: bool = False) -> dict:
    effective_unlocked = result.unlocked or force_unlock

    primary = get_category(result.primary_category)
    secondary = get_category(result.secondary_category)

    if not effective_unlocked:
        # Free tier (PRD 6.4): primary shown in full (name/description) but curriculum+resources
        # stay locked; secondary is name-only.
        primary = {**primary, "curriculum": None, "resources": None}
        secondary = {
            "key": secondary["key"],
            "name": secondary["name"],
            "track": secondary["track"],
            "focus": None,
            "duration": None,
            "phase_1": secondary["phase_1"],
            "curriculum": None,
            "resources": None,
        }

    return {
        "id": result.id,
        "track": result.track,
        "unlocked": effective_unlocked,
        "close_call": result.close_call,
        "close_call_message": (
            "You scored closely across multiple paths — this means you have versatile strengths. "
            "A consultation with Sharafdeen will help you make the best choice."
            if result.close_call
            else None
        ),
        "primary": primary,
        "secondary": secondary,
        "scores": result.scores,
        "created_at": result.created_at,
    }
