from fastapi import APIRouter, Depends

from app import models

from app.core.security import get_current_user


router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.get("/")
async def get_orders(
    current_user: models.Users = Depends(
        get_current_user
    )
):
    return {
        "user_id": current_user.id,
        "orders": []
    }