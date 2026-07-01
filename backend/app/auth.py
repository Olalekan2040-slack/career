"""Lightweight email+password auth: PBKDF2 password hashing + signed, expiring tokens.

No external JWT dependency — uses itsdangerous (already a dependency) for
tamper-proof, time-limited tokens carrying just the user id.
"""

import hashlib
import hmac
import os

from fastapi import Depends, Header, HTTPException
from itsdangerous import BadSignature, SignatureExpired, URLSafeTimedSerializer
from sqlalchemy.orm import Session

from . import models
from .config import settings
from .database import get_db

TOKEN_MAX_AGE_SECONDS = 60 * 60 * 24 * 30  # 30 days
_serializer = URLSafeTimedSerializer(settings.secret_key, salt="auth-token")


def hash_password(password: str) -> str:
    salt = os.urandom(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 200_000)
    return f"{salt.hex()}${digest.hex()}"


def verify_password(password: str, stored_hash: str) -> bool:
    try:
        salt_hex, digest_hex = stored_hash.split("$")
    except ValueError:
        return False
    salt = bytes.fromhex(salt_hex)
    expected = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 200_000)
    return hmac.compare_digest(expected.hex(), digest_hex)


def create_token(user_id: str) -> str:
    return _serializer.dumps({"user_id": user_id})


def _decode_token(token: str) -> str | None:
    try:
        data = _serializer.loads(token, max_age=TOKEN_MAX_AGE_SECONDS)
        return data.get("user_id")
    except (BadSignature, SignatureExpired):
        return None


def get_current_user(
    authorization: str | None = Header(None), db: Session = Depends(get_db)
) -> models.User:
    user = get_optional_user(authorization, db)
    if user is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return user


def get_optional_user(
    authorization: str | None = Header(None), db: Session = Depends(get_db)
) -> models.User | None:
    if not authorization or not authorization.startswith("Bearer "):
        return None
    token = authorization.removeprefix("Bearer ").strip()
    user_id = _decode_token(token)
    if not user_id:
        return None
    return db.get(models.User, user_id)
