from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas
from ..data.categories import CATEGORIES
from ..database import get_db
from ..email_service import render_waitlist_email, send_email

router = APIRouter(prefix="/api/waitlist", tags=["waitlist"])


@router.post("")
def join_waitlist(payload: schemas.WaitlistJoin, db: Session = Depends(get_db)):
    category = CATEGORIES.get(payload.category_key)
    if category is None:
        raise HTTPException(status_code=404, detail="Unknown category")

    entry = models.WaitlistEntry(email=payload.email.lower().strip(), category_key=payload.category_key)
    db.add(entry)
    db.commit()

    try:
        html = render_waitlist_email(category["name"])
        send_email(payload.email, f"You'll be notified when {category['name']} launches", html)
    except Exception as exc:  # pragma: no cover
        print(f"[waitlist] failed to send confirmation email: {exc}")

    return {"joined": True}
