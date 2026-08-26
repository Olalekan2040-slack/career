from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db
from ..result_builder import build_result_out

router = APIRouter(prefix="/api/qeezara-admin", tags=["admin"])


@router.get("/users", response_model=list[schemas.AdminUserOut])
def list_users(
    db: Session = Depends(get_db),
):
    return db.query(models.User).order_by(models.User.created_at.desc()).all()


@router.get("/leads", response_model=list[schemas.AdminLeadOut])
def list_leads(
    db: Session = Depends(get_db),
):
    return db.query(models.Lead).order_by(models.Lead.created_at.desc()).all()


@router.get("/assessment-results", response_model=list[schemas.AdminAssessmentResultOut])
def list_assessment_results(
    db: Session = Depends(get_db),
):
    """Get all assessment results with lead info and recommendations for admin export"""
    results = (
        db.query(models.Result)
        .join(models.AssessmentResponse, models.Result.response_id == models.AssessmentResponse.id)
        .join(models.Lead, models.AssessmentResponse.lead_id == models.Lead.id)
        .order_by(models.Result.created_at.desc())
        .all()
    )

    output = []
    for result in results:
        lead = result.response.lead
        result_out = build_result_out(result)
        output.append(
            schemas.AdminAssessmentResultOut(
                result_id=result.id,
                lead_name=lead.name,
                lead_email=lead.email,
                submitted_at=result.created_at,
                close_call=result.close_call,
                recommendations=result_out["recommendations"],
            )
        )
    return output
