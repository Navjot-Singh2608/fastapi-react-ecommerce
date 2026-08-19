from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status

from app import models

from app.database import get_db
from app.schemas import CreateUserRequest, UserResponse, Token

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
async def register_user(
    user_request: CreateUserRequest,
    db: Session = Depends(get_db)
):
    print("you are here......")

    existing_username = (
        db.query(models.Users)
        .filter(
            models.Users.username
            == user_request.username
        )
        .first()
    )

    if existing_username:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    existing_email = (
        db.query(models.Users)
        .filter(
            models.Users.email
            == user_request.email
        )
        .first()
    )

    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )



    user = models.Users(
        username=user_request.username,
        email=user_request.email,
        first_name=user_request.first_name,
        last_name=user_request.last_name,

        hashed_password=hash_password(
            user_request.password
        ),

        is_active=True
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


@router.post(
    "/token",
    response_model=Token
)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    user = (
        db.query(models.Users)
        .filter(
            models.Users.username
            == form_data.username
        )
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    if not verify_password(
        form_data.password,
        user.hashed_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    token = create_access_token(
        username=user.username,
        user_id=user.id
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }