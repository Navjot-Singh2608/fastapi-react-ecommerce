from fastapi import APIRouter, Depends

from app import models

from app.core.security import get_current_user


router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)


@router.get("/")
async def get_cart(
    current_user: models.Users = Depends(
        get_current_user
    )
):
    return {
        "user_id": current_user.id,
        "items": []
    }