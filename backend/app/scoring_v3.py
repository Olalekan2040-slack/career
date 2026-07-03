"""Scoring engine for the Comprehensive Question Bank (88 items, 5 section types).

Pipeline: answers -> per-competency raw/max totals -> normalized competency
profile (0-1 per competency) -> dot product against the derived career matrix
-> ranked career list -> top N as recommendations, each with plain-language
reasons drawn from its highest-contributing competencies.

Because users may skip any question, every competency is normalized against
the maximum achievable score from only the questions actually answered — so
partial completion still yields a fair, comparable profile rather than
penalizing skipped competencies as zero-vs-full-scale.
"""

from .data.career_matrix import CAREER_MATRIX
from .data.competencies import COMPETENCIES
from .data.questions_v3 import (
    FORCED_CHOICE_QUESTIONS,
    LIKERT_QUESTIONS,
    RANKING_QUESTIONS,
    SCENARIO_QUESTIONS,
    SITUATIONAL_QUESTIONS,
)
from .data.shortlist import SHORTLIST, build_entry_note

SHORTLIST_MATRIX = {key: weights for key, weights in CAREER_MATRIX.items() if key in SHORTLIST}

RANK_MULTIPLIERS = [1.0, 0.75, 0.5, 0.25]

LIKERT_BY_ID = {q["id"]: q for q in LIKERT_QUESTIONS}
FORCED_CHOICE_BY_ID = {q["id"]: q for q in FORCED_CHOICE_QUESTIONS}
SCENARIO_BY_ID = {q["id"]: q for q in SCENARIO_QUESTIONS}
SITUATIONAL_BY_ID = {q["id"]: q for q in SITUATIONAL_QUESTIONS}
RANKING_BY_ID = {q["id"]: q for q in RANKING_QUESTIONS}


class ScoringError(ValueError):
    pass


def _apply_single_choice(raw: dict, max_possible: dict, questions_by_id: dict, answers: dict) -> None:
    for qid, choice_key in answers.items():
        question = questions_by_id.get(qid)
        if question is None:
            continue
        option = question["options"].get(choice_key)
        if option is None:
            continue
        for competency, weight in option["competencies"].items():
            raw[competency] = raw.get(competency, 0.0) + weight
            max_possible[competency] = max_possible.get(competency, 0.0) + weight


def _apply_likert(raw: dict, max_possible: dict, answers: dict) -> None:
    for qid, rating in answers.items():
        question = LIKERT_BY_ID.get(qid)
        if question is None:
            continue
        rating = max(1, min(5, int(rating)))
        for competency, weight in question["competencies"].items():
            raw[competency] = raw.get(competency, 0.0) + rating * weight
            max_possible[competency] = max_possible.get(competency, 0.0) + 5 * weight


def _apply_ranking(raw: dict, max_possible: dict, answers: dict) -> None:
    for qid, ordered_item_keys in answers.items():
        question = RANKING_BY_ID.get(qid)
        if question is None:
            continue
        for position, item_key in enumerate(ordered_item_keys[:4]):
            item = question["items"].get(item_key)
            if item is None:
                continue
            multiplier = RANK_MULTIPLIERS[position]
            for competency, weight in item["competencies"].items():
                raw[competency] = raw.get(competency, 0.0) + multiplier * weight
                max_possible[competency] = max_possible.get(competency, 0.0) + weight


def compute_competency_profile(answers: dict) -> dict[str, float]:
    """Returns a 0-1 ratio per competency code from whatever sections were answered."""
    raw: dict[str, float] = {}
    max_possible: dict[str, float] = {}

    _apply_likert(raw, max_possible, answers.get("likert", {}) or {})
    _apply_single_choice(raw, max_possible, FORCED_CHOICE_BY_ID, answers.get("forced_choice", {}) or {})
    _apply_single_choice(raw, max_possible, SCENARIO_BY_ID, answers.get("scenario", {}) or {})
    _apply_single_choice(raw, max_possible, SITUATIONAL_BY_ID, answers.get("situational", {}) or {})
    _apply_ranking(raw, max_possible, answers.get("ranking", {}) or {})

    profile = {}
    for competency in COMPETENCIES:
        total = max_possible.get(competency, 0.0)
        profile[competency] = (raw.get(competency, 0.0) / total) if total > 0 else 0.0
    return profile


def total_answered_count(answers: dict) -> int:
    return sum(len(answers.get(section, {}) or {}) for section in ("likert", "forced_choice", "scenario", "situational", "ranking"))


def rank_careers(profile: dict[str, float]) -> list[tuple[str, float]]:
    scores = {}
    for career, weights in SHORTLIST_MATRIX.items():
        scores[career] = sum(profile.get(competency, 0.0) * weight for competency, weight in weights.items())
    return sorted(scores.items(), key=lambda kv: kv[1], reverse=True)


def build_reason(career_key: str, profile: dict[str, float], limit: int = 2) -> str:
    weights = SHORTLIST_MATRIX.get(career_key, {})
    contributions = sorted(
        ((competency, profile.get(competency, 0.0) * weight) for competency, weight in weights.items()),
        key=lambda kv: kv[1],
        reverse=True,
    )
    top = [COMPETENCIES[code] for code, contribution in contributions[:limit] if contribution > 0]
    if not top:
        return "Your overall response pattern is the closest fit among the careers assessed."
    if len(top) == 1:
        return f"Your strength in {top[0]} closely matches this career."
    return f"Your strengths in {' and '.join(top)} closely match this career."


def compute_recommendations(answers: dict, count: int, tech_exposure: str | None = None) -> list[dict]:
    if total_answered_count(answers) == 0:
        raise ScoringError("Please answer at least one question before submitting.")

    profile = compute_competency_profile(answers)
    ranked = rank_careers(profile)

    recommendations = []
    for career_key, score in ranked[:count]:
        recommendations.append(
            {
                "career_key": career_key,
                "score": round(score, 4),
                "reason": build_reason(career_key, profile),
                "entry_note": build_entry_note(career_key, tech_exposure),
            }
        )
    return recommendations
