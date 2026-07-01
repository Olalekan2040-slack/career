"""Scoring engine implementing the routing + recommendation logic from Question Bank v2.0."""

from .data.questions import (
    ORIENTATION_QUESTIONS,
    TRACK_A_QUESTIONS,
    TRACK_B_QUESTIONS,
    TRACK_A_CATEGORIES,
    TRACK_B_CATEGORIES,
)

DIFFERENTIATION_THRESHOLD = 3
CLOSE_CALL_MESSAGE = (
    "You scored closely across multiple paths — this means you have versatile strengths. "
    "A consultation with Sharafdeen will help you make the best choice."
)


class ScoringError(ValueError):
    pass


def _questions_by_id(questions):
    return {q["id"]: q for q in questions}


ORIENTATION_BY_ID = _questions_by_id(ORIENTATION_QUESTIONS)
TRACK_A_BY_ID = _questions_by_id(TRACK_A_QUESTIONS)
TRACK_B_BY_ID = _questions_by_id(TRACK_B_QUESTIONS)


def _sum_scores(questions_by_id: dict, answers: dict, dimensions: list[str]) -> dict:
    totals = {dim: 0 for dim in dimensions}
    for question_id, option_key in answers.items():
        question = questions_by_id.get(question_id)
        if question is None:
            continue
        option = question["options"].get(option_key)
        if option is None:
            continue
        for dim, value in option["scores"].items():
            if dim in totals:
                totals[dim] += value
    return totals


def determine_track(orientation_answers: dict) -> str:
    """Returns 'A' or 'B' per the routing logic in Section 1 of the question bank."""
    dims = _sum_scores(ORIENTATION_BY_ID, orientation_answers, ["CD", "NC", "CR", "LG", "PP", "DT"])
    if dims["CD"] > dims["NC"]:
        return "A"
    if dims["NC"] > dims["CD"]:
        return "B"
    # Tiebreaker: LG+DT vs CR+PP
    analytical = dims["LG"] + dims["DT"]
    creative_people = dims["CR"] + dims["PP"]
    if analytical > creative_people:
        return "A"
    if creative_people > analytical:
        return "B"
    return "B"  # still tied -> default to Track B


def score_deep_dive(track: str, deep_dive_answers: dict) -> dict:
    if track == "A":
        return _sum_scores(TRACK_A_BY_ID, deep_dive_answers, TRACK_A_CATEGORIES)
    if track == "B":
        return _sum_scores(TRACK_B_BY_ID, deep_dive_answers, TRACK_B_CATEGORIES)
    raise ScoringError(f"Unknown track: {track}")


def rank_categories(scores: dict) -> list[tuple[str, int]]:
    return sorted(scores.items(), key=lambda kv: kv[1], reverse=True)


def compute_result(orientation_answers: dict, deep_dive_answers: dict) -> dict:
    """Runs the full two-stage scoring pipeline and returns primary/secondary + metadata."""
    track = determine_track(orientation_answers)
    scores = score_deep_dive(track, deep_dive_answers)
    ranked = rank_categories(scores)

    primary_key, primary_score = ranked[0]
    secondary_key, secondary_score = ranked[1]

    close_call = (primary_score - secondary_score) < DIFFERENTIATION_THRESHOLD

    return {
        "track": track,
        "scores": scores,
        "primary_category": primary_key,
        "secondary_category": secondary_key,
        "close_call": close_call,
        "close_call_message": CLOSE_CALL_MESSAGE if close_call else None,
    }
