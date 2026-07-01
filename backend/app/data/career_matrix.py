"""Derives the Competency -> Career mapping matrix from the question bank itself.

The source document (Comprehensive_Question_Bank_Psychometric.docx) explicitly
notes that a separate 24x70 mapping matrix is the "next required artefact" for
turning competency totals into career scores, but does not provide one. Rather
than inventing arbitrary weights, this module derives the matrix directly from
data already in the question bank: every question/option/ranking-item lists
both the competencies it measures (with weights) and the careers it signals
("careers_influenced"). Summing those signals per career and normalizing each
career's row to sum to 1 produces a defensible, fully-traceable matrix without
needing a second hand-authored artefact.
"""

from collections import defaultdict

from .questions_v3 import (
    FORCED_CHOICE_QUESTIONS,
    LIKERT_QUESTIONS,
    RANKING_QUESTIONS,
    SCENARIO_QUESTIONS,
    SITUATIONAL_QUESTIONS,
)


def _accumulate(matrix: dict, careers: list[str], competencies: dict[str, int]) -> None:
    for career in careers:
        for competency, weight in competencies.items():
            matrix[career][competency] += weight


def _build_raw_matrix() -> dict[str, dict[str, float]]:
    matrix: dict[str, dict[str, float]] = defaultdict(lambda: defaultdict(float))

    for question in LIKERT_QUESTIONS:
        _accumulate(matrix, question["careers_influenced"], question["competencies"])

    for section in (FORCED_CHOICE_QUESTIONS, SCENARIO_QUESTIONS, SITUATIONAL_QUESTIONS):
        for question in section:
            for option in question["options"].values():
                _accumulate(matrix, option["careers_influenced"], option["competencies"])

    for question in RANKING_QUESTIONS:
        for item in question["items"].values():
            _accumulate(matrix, item["careers_influenced"], item["competencies"])

    return matrix


def _normalize(matrix: dict[str, dict[str, float]]) -> dict[str, dict[str, float]]:
    normalized = {}
    for career, weights in matrix.items():
        total = sum(weights.values())
        if total <= 0:
            normalized[career] = {}
            continue
        normalized[career] = {competency: weight / total for competency, weight in weights.items()}
    return normalized


# These 5 careers from the Career Legend are never referenced in any question's
# "careers_influenced" hints (an omission in the source question bank), so they
# have no derivable data. Hand-authored profiles based on their closest
# neighbouring careers keep the full 69-career taxonomy scorable.
_MANUAL_OVERRIDES: dict[str, dict[str, float]] = {
    "MAD": {"SYS": 0.3, "TCUR": 0.3, "CR": 0.2, "VT": 0.2},  # Mobile App Development
    "DAD": {"SYS": 0.4, "TCUR": 0.3, "DET": 0.3},  # Desktop Application Development
    "GDV": {"CR": 0.3, "VT": 0.25, "SYS": 0.25, "INNOV": 0.2},  # Game Development
    "BLK": {"SYS": 0.3, "TCUR": 0.3, "RISK": 0.2, "ANA": 0.2},  # Blockchain Development
    "W3": {"SYS": 0.25, "TCUR": 0.25, "INNOV": 0.25, "RISK": 0.25},  # Web3 Development
}

CAREER_MATRIX: dict[str, dict[str, float]] = {**_normalize(_build_raw_matrix()), **_MANUAL_OVERRIDES}


def top_competencies_for_career(career_key: str, limit: int = 3) -> list[str]:
    weights = CAREER_MATRIX.get(career_key, {})
    ranked = sorted(weights.items(), key=lambda kv: kv[1], reverse=True)
    return [code for code, _ in ranked[:limit]]
