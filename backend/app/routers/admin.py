from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import models, schemas
from ..auth import get_current_admin
from ..database import get_db

router = APIRouter(prefix="/api/admin", tags=["admin"])


@router.get("/users", response_model=list[schemas.AdminUserOut])
def list_users(
    db: Session = Depends(get_db),
    _admin: models.User = Depends(get_current_admin),
):
    return db.query(models.User).order_by(models.User.created_at.desc()).all()
