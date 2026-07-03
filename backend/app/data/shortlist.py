"""The active recommendation shortlist for the beginner-focused platform.

The full 69-career taxonomy in careers.py / career_matrix.py stays intact as
reference data, but only these 28 careers are ever surfaced as
recommendations — curated for people who are new to tech and need a
short, confident list of realistic next steps rather than an exhaustive
catalogue.

ADVANCED_ENTRY maps a subset of the shortlist to a gentler starting point.
These are careers that usually assume some prior programming/technical
exposure — if a total beginner's answers still point strongly toward one,
the result shows a caveat naming the suggested starting point instead of
silently recommending a path they may not be ready to jump straight into.
"""

SHORTLIST = {
    "FSD",  # Full-Stack Web Development
    "FWD",  # Frontend Web Development
    "BWD",  # Backend Web Development
    "AI",   # Artificial Intelligence
    "ML",   # Machine Learning
    "UX",   # UI/UX Design (includes UX research)
    "GD",   # Graphic Design
    "VE",   # Video Editing
    "CW",   # Content Writing
    "SMM",  # Social Media Management
    "VA",   # Virtual Assistance
    "DAN",  # Data Analysis
    "DS",   # Data Science
    "CLD",  # Cloud Computing
    "CYB",  # Cybersecurity
    "MAD",  # Mobile App Development
    "QA",   # Software Testing (QA)
    "ANI",  # Animation
    "DE",   # Data Engineering
    "DM",   # Digital Marketing
    "SEO",  # Search Engine Optimization
    "TW",   # Technical Writing
    "PM",   # Product Management
    "PJM",  # Project Management
    "DVO",  # DevOps Engineering
    "ITS",  # IT Support
    "MG",   # Motion Graphics Design
    "CPW",  # Copywriting
}

# career_key -> suggested easier starting point + why
ADVANCED_ENTRY = {
    "FSD": "FWD",
    "BWD": "FWD",
    "AI": "DAN",
    "ML": "DAN",
    "DS": "DAN",
    "CLD": "ITS",
    "CYB": "ITS",
    "MAD": "FWD",
    "DE": "DAN",
    "DVO": "ITS",
}


def is_advanced_entry(career_key: str) -> bool:
    return career_key in ADVANCED_ENTRY


def easier_alternative(career_key: str) -> str | None:
    return ADVANCED_ENTRY.get(career_key)


def build_entry_note(career_key: str, tech_exposure: str | None) -> str | None:
    """Returns a caveat string if this career is an advanced-entry path and the
    respondent flagged no prior tech exposure — None otherwise."""
    if tech_exposure != "none":
        return None
    alt_key = ADVANCED_ENTRY.get(career_key)
    if alt_key is None:
        return None
    from .careers import CAREERS  # local import avoids a module load-order cycle

    alt_name = CAREERS[alt_key]["name"]
    return (
        f"This path is usually easier to start with some prior programming or technical exposure. "
        f"Many people build a foundation with something like {alt_name} first."
    )
