"""Background intake — collected before the adaptive assessment begins.

age_range, education_level, and gender are for context/reporting only and
never feed scoring. field_of_study and tech_exposure drive the "advanced
entry" caveat (see shortlist.py). interest_area drives the first stage of
adaptive question selection (see adaptive.py) — instead of a flat random
sample, early questions are weighted toward competencies related to what the
respondent says excites them, independent of tech exposure.
"""

INTAKE_FIELDS = [
    {
        "key": "age_range",
        "label": "What's your age range?",
        "required": True,
        "options": [
            {"key": "under_18", "label": "Under 18"},
            {"key": "18_24", "label": "18–24"},
            {"key": "25_34", "label": "25–34"},
            {"key": "35_44", "label": "35–44"},
            {"key": "45_plus", "label": "45+"},
        ],
    },
    {
        "key": "education_level",
        "label": "What's your highest level of education?",
        "required": True,
        "options": [
            {"key": "secondary", "label": "Secondary / High school"},
            {"key": "some_college", "label": "Some college/university, no degree yet"},
            {"key": "bachelors", "label": "Bachelor's degree"},
            {"key": "masters_or_higher", "label": "Master's degree or higher"},
            {"key": "vocational", "label": "Vocational / Technical training"},
            {"key": "other", "label": "Other"},
        ],
    },
    {
        "key": "field_of_study",
        "label": "What field is your background in (school or work)?",
        "required": True,
        "options": [
            {"key": "computer_science_it", "label": "Computer Science / IT"},
            {"key": "engineering", "label": "Engineering"},
            {"key": "business_management", "label": "Business / Management"},
            {"key": "social_sciences", "label": "Social Sciences"},
            {"key": "arts_humanities", "label": "Arts / Humanities"},
            {"key": "natural_sciences", "label": "Natural Sciences"},
            {"key": "medicine_health", "label": "Medicine / Health"},
            {"key": "law", "label": "Law"},
            {"key": "other_none", "label": "Other / None"},
        ],
    },
    {
        "key": "tech_exposure",
        "label": "Have you done any of these before: written code, used design software professionally, worked in IT/tech support, or studied a tech-related course?",
        "required": True,
        "options": [
            {"key": "none", "label": "No, none of these"},
            {"key": "some", "label": "A little — I've tried one or two"},
            {"key": "significant", "label": "Yes, I have real experience in at least one"},
        ],
    },
    {
        "key": "interest_area",
        "label": "Even outside of tech, which of these excites you most?",
        "required": True,
        "options": [
            {"key": "technology_systems", "label": "Technology & how systems work"},
            {"key": "business_strategy", "label": "Business & strategy"},
            {"key": "arts_creativity", "label": "Arts & creativity"},
            {"key": "people_communication", "label": "People & communication"},
            {"key": "science_research", "label": "Science & research"},
            {"key": "hands_on_practical", "label": "Hands-on, practical work"},
        ],
    },
    {
        "key": "gender",
        "label": "Gender (optional)",
        "required": False,
        "options": [
            {"key": "male", "label": "Male"},
            {"key": "female", "label": "Female"},
            {"key": "other", "label": "Other"},
            {"key": "prefer_not_to_say", "label": "Prefer not to say"},
        ],
    },
]

# interest_area -> competencies to weight toward during early question selection
INTEREST_COMPETENCY_MAP = {
    "technology_systems": ["SYS", "TCUR", "LR"],
    "business_strategy": ["BUS", "ENTP", "LEAD"],
    "arts_creativity": ["CR", "VT", "INNOV"],
    "people_communication": ["COM", "EMP", "TEACH", "COLLAB"],
    "science_research": ["ANA", "RES", "NR", "CUR"],
    "hands_on_practical": ["DET", "PER", "ADAPT"],
}
