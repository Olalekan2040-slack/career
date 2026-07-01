from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import models, schemas
from ..auth import get_current_user
from ..database import get_db
from ..result_builder import build_result_out

router = APIRouter(prefix="/api/dashboard", tags=["dashboard"])


@router.get("/results", response_model=list[schemas.DashboardResultOut])
def list_my_results(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    results = (
        db.query(models.Result)
        .join(models.AssessmentResponse)
        .join(models.Lead)
        .filter(models.Lead.user_id == current_user.id)
        .order_by(models.Result.created_at.desc())
        .all()
    )
    return [build_result_out(result, force_unlock=True) for result in results]
