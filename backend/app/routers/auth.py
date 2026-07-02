from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas
from ..auth import create_token, get_current_user, hash_password, sync_admin_flag, verify_password
from ..database import get_db

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/signup", response_model=schemas.TokenResponse)
def signup(payload: schemas.SignupRequest, db: Session = Depends(get_db)):
    email = payload.email.lower().strip()
    existing = db.query(models.User).filter(models.User.email == email).first()
    if existing is not None:
        raise HTTPException(status_code=409, detail="An account with this email already exists")

    user = models.User(name=payload.name.strip(), email=email, password_hash=hash_password(payload.password))
    sync_admin_flag(user)
    db.add(user)
    db.commit()
    db.refresh(user)

    return {"access_token": create_token(user.id), "user": user}


@router.post("/login", response_model=schemas.TokenResponse)
def login(payload: schemas.LoginRequest, db: Session = Depends(get_db)):
    email = payload.email.lower().strip()
    user = db.query(models.User).filter(models.User.email == email).first()
    if user is None or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Incorrect email or password")

    sync_admin_flag(user)
    db.commit()

    return {"access_token": create_token(user.id), "user": user}


@router.get("/me", response_model=schemas.UserOut)
def me(current_user: models.User = Depends(get_current_user)):
    return current_user
