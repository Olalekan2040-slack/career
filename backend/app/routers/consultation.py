from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/api/consultation", tags=["consultation"])


@router.post("", response_model=schemas.ConsultationOut)
def create_consultation(payload: schemas.ConsultationCreate, db: Session = Depends(get_db)):
    lead = db.get(models.Lead, payload.lead_id)
    if lead is None:
        raise HTTPException(status_code=404, detail="Lead not found")

    consultation = models.Consultation(
        lead_id=lead.id,
        preferred_time=payload.preferred_time,
        note=payload.note,
        status="requested",
    )
    db.add(consultation)
    db.commit()
    db.refresh(consultation)
    return consultation
