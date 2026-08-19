from datetime import datetime, timedelta, timezone

import jwt

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from pwdlib import PasswordHash

from sqlalchemy.orm import Session

from starlette import status

from app import models

from app.database import get_db

from app.core.config import (
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)


# --------------------------------------------------
# PASSWORD HASHING
# --------------------------------------------------

password_hash = PasswordHash.recommended()


def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    """
    Compare plain password with stored hashed password.
    """

    return password_hash.verify(
        plain_password,
        hashed_password
    )


# --------------------------------------------------
# OAUTH2
# --------------------------------------------------

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/token"
)

def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    return password_hash.verify(
        plain_password,
        hashed_password
    )



# --------------------------------------------------
# CREATE JWT TOKEN
# --------------------------------------------------

def create_access_token(
    username: str,
    user_id: int
) -> str:

    expire = (
        datetime.now(timezone.utc)
        + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
    )

    payload = {
        "sub": username,
        "id": user_id,
        "exp": expire,
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


# --------------------------------------------------
# GET CURRENT LOGGED-IN USER
# --------------------------------------------------

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={
            "WWW-Authenticate": "Bearer"
        }
    )

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")
        user_id = payload.get("id")

        if username is None:
            raise credentials_exception

        if user_id is None:
            raise credentials_exception

    except jwt.InvalidTokenError:
        raise credentials_exception

    user = (
        db.query(models.Users)
        .filter(
            models.Users.id == user_id
        )
        .first()
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user"
        )

    return user