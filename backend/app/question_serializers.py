"""Shared question -> API response serialization, used by both the static
/api/questions listing and the adaptive /api/assessment/next endpoint."""


def serialize_question(section: str, question: dict) -> dict:
    if section == "likert":
        return {"id": question["id"], "text": question["text"]}
    if section == "ranking":
        return {
            "id": question["id"],
            "text": question["text"],
            "items": [
                {"key": key, "text": item["text"], "hint": item.get("hint")}
                for key, item in question["items"].items()
            ],
        }
    return {
        "id": question["id"],
        "text": question["text"],
        "options": [
            {"key": key, "text": opt["text"], "hint": opt.get("hint")}
            for key, opt in question["options"].items()
        ],
    }
