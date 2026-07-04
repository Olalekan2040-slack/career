from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/api/leads", tags=["leads"])


@router.post("", response_model=schemas.LeadOut)
def create_lead(payload: schemas.LeadCreate, db: Session = Depends(get_db)):
    lead = models.Lead(
        name=payload.name.strip(),
        email=payload.email.lower().strip(),
        consent_given=payload.consent_given,
    )
    db.add(lead)
    db.commit()
    db.refresh(lead)
    return lead
