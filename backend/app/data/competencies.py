"""The 24 underlying competencies measured by the Comprehensive Question Bank.

Questions score these competencies directly; competency totals are then
projected onto the 70-career space via the derived career mapping matrix
(see career_matrix.py).
"""

COMPETENCIES = {
    "LR": "Logical Reasoning",
    "NR": "Numerical Reasoning",
    "CR": "Creativity",
    "VT": "Visual Thinking",
    "COM": "Communication",
    "IND": "Independence",
    "WR": "Writing Ability",
    "TCUR": "Technical Curiosity",
    "LEAD": "Leadership",
    "ORG": "Organization",
    "CUR": "Curiosity",
    "PER": "Persistence",
    "RES": "Research Ability",
    "ADAPT": "Adaptability",
    "DET": "Detail Orientation",
    "RISK": "Risk Tolerance",
    "EMP": "Empathy",
    "INNOV": "Innovation",
    "SYS": "Systems Thinking",
    "ANA": "Analytical / Pattern Thinking",
    "BUS": "Business Thinking",
    "TEACH": "Teaching Ability",
    "ENTP": "Entrepreneurship",
    "COLLAB": "Collaboration",
}

COMPETENCY_CODES = list(COMPETENCIES.keys())
