from fastapi import APIRouter, Depends

from app import models

from app.schemas import UserResponse
from app.core.security import get_current_user


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get(
    "/me",
    response_model=UserResponse
)
async def get_logged_in_user(
    current_user: models.Users = Depends(
        get_current_user
    )
):
    return current_user