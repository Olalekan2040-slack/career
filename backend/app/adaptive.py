"""Adaptive question selection and stopping logic.

This is a practical, honest approximation of adaptive testing — not full
Item Response Theory (which needs item parameters calibrated from prior
response data we don't have yet). Two stages:

  Stage 1 (first STAGE1_QUESTION_COUNT questions): weight selection toward
  competencies related to the respondent's stated interest_area from intake,
  so the test branches on their background from question 1 instead of
  sampling randomly.

  Stage 2 (afterward): recompute the running competency profile after every
  answer, find which competencies most separate the current top-ranked
  shortlist careers, and select the next unanswered question that scores
  heavily on those — i.e., whichever question is most likely to change or
  confirm the current leading candidates.

Stopping is a floor/cap/confidence rule (see should_stop) rather than a fixed
question count, per the "flow of the respondent's answers" requirement.
"""

import random

from .data.competencies import COMPETENCY_CODES
from .data.intake import INTEREST_COMPETENCY_MAP
from .data.questions_v3 import (
    FORCED_CHOICE_QUESTIONS,
    LIKERT_QUESTIONS,
    RANKING_QUESTIONS,
    SCENARIO_QUESTIONS,
    SITUATIONAL_QUESTIONS,
)
from .scoring_v3 import SHORTLIST_MATRIX, compute_competency_profile, rank_careers

STAGE1_QUESTION_COUNT = 8
MIN_QUESTIONS = 12
MAX_QUESTIONS = 30
TIME_CAP_SECONDS = 270  # 4.5 minutes — leaves buffer under the 5-minute target
CONFIDENCE_GAP = 0.12

ALL_SECTIONS = {
    "likert": LIKERT_QUESTIONS,
    "forced_choice": FORCED_CHOICE_QUESTIONS,
    "scenario": SCENARIO_QUESTIONS,
    "situational": SITUATIONAL_QUESTIONS,
    "ranking": RANKING_QUESTIONS,
}

def _question_competency_weight(section: str, question: dict) -> dict[str, float]:
    """Average competency weight across a question's options/items, used to
    score how relevant a question is to a set of target competencies."""
    if section == "likert":
        return question["competencies"]

    groups = question["options"].values() if section != "ranking" else question["items"].values()
    totals: dict[str, float] = {}
    count = 0
    for group in groups:
        count += 1
        for competency, weight in group["competencies"].items():
            totals[competency] = totals.get(competency, 0.0) + weight
    return {c: w / count for c, w in totals.items()} if count else {}


def _all_unanswered(answered_ids: set[str]):
    for section, questions in ALL_SECTIONS.items():
        for question in questions:
            if question["id"] not in answered_ids:
                yield section, question


def _answered_ids(answers: dict) -> set[str]:
    ids = set()
    for section in ALL_SECTIONS:
        ids.update((answers.get(section) or {}).keys())
    return ids


def _pick_weighted(scored_candidates: list[tuple[float, str, dict]]) -> tuple[str, dict]:
    """Picks from the top few candidates with a little randomness so repeat
    attempts don't always ask the exact same sequence."""
    scored_candidates.sort(key=lambda item: item[0], reverse=True)
    top = scored_candidates[: min(5, len(scored_candidates))]
    _, section, question = random.choice(top)
    return section, question


def select_next_question(intake: dict, answers: dict, skipped_ids: set[str] | None = None) -> dict | None:
    answered_ids = _answered_ids(answers)
    total_answered = len(answered_ids)
    excluded_ids = answered_ids | (skipped_ids or set())
    candidates = list(_all_unanswered(excluded_ids))
    if not candidates:
        return None

    if total_answered < STAGE1_QUESTION_COUNT:
        target_competencies = set(INTEREST_COMPETENCY_MAP.get(intake.get("interest_area"), []))
        scored = []
        for section, question in candidates:
            weights = _question_competency_weight(section, question)
            affinity = sum(weights.get(c, 0.0) for c in target_competencies)
            scored.append((affinity, section, question))
    else:
        profile = compute_competency_profile(answers)
        ranked = rank_careers(profile)
        top5_keys = [key for key, _ in ranked[:5]]
        variance = {}
        for competency in COMPETENCY_CODES:
            values = [SHORTLIST_MATRIX.get(key, {}).get(competency, 0.0) for key in top5_keys]
            mean = sum(values) / len(values) if values else 0.0
            variance[competency] = sum((v - mean) ** 2 for v in values) / len(values) if values else 0.0

        scored = []
        for section, question in candidates:
            weights = _question_competency_weight(section, question)
            discriminative_value = sum(variance.get(c, 0.0) * w for c, w in weights.items())
            scored.append((discriminative_value, section, question))

    section, question = _pick_weighted(scored)
    return {"section": section, "question": question}


def should_stop(answers: dict, elapsed_seconds: float) -> bool:
    total_answered = len(_answered_ids(answers))

    if total_answered == 0:
        return False
    if elapsed_seconds >= TIME_CAP_SECONDS:
        return True
    if total_answered >= MAX_QUESTIONS:
        return True
    if total_answered < MIN_QUESTIONS:
        return False

    profile = compute_competency_profile(answers)
    ranked = rank_careers(profile)
    if len(ranked) < 5:
        return True
    top_score = ranked[0][1]
    fifth_score = ranked[4][1]
    return (top_score - fifth_score) >= CONFIDENCE_GAP
