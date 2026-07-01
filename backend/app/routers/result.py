from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas
from ..auth import get_optional_user
from ..database import get_db
from ..result_builder import build_result_out

router = APIRouter(prefix="/api/result", tags=["result"])


@router.get("/{result_id}", response_model=schemas.ResultOut)
def get_result(
    result_id: str,
    db: Session = Depends(get_db),
    current_user: models.User | None = Depends(get_optional_user),
):
    result = db.get(models.Result, result_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Result not found")

    lead = result.response.lead
    is_owner = current_user is not None and lead.user_id == current_user.id
    return build_result_out(result, force_unlock=is_owner)
