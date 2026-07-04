from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import schemas
from ..database import get_db
from .. import models
from ..result_builder import build_result_out

router = APIRouter(prefix="/api/result", tags=["result"])


@router.get("/{result_id}", response_model=schemas.ResultOut)
def get_result(result_id: str, db: Session = Depends(get_db)):
    result = db.get(models.Result, result_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Result not found")
    return build_result_out(result)
