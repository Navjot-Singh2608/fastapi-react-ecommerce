from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session
from starlette import status

from app import models

from app.database import get_db
from app.schemas import (
    ProductRequest,
    ProductResponse
)

from app.core.security import get_current_user


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


# --------------------------------
# GET ALL PRODUCTS
# Public endpoint
# --------------------------------

@router.get(
    "/",
    response_model=list[ProductResponse]
)
async def get_all_products(
    db: Session = Depends(get_db)
):

    products = (
        db.query(models.Products)
        .filter(
            models.Products.is_active == True
        )
        .all()
    )

    return products


# --------------------------------
# GET PRODUCT BY ID
# Public endpoint
# --------------------------------

@router.get(
    "/{product_id}",
    response_model=ProductResponse
)
async def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):

    product = (
        db.query(models.Products)
        .filter(
            models.Products.id == product_id
        )
        .first()
    )

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


# --------------------------------
# CREATE PRODUCT
# Requires JWT
# --------------------------------

@router.post(
    "/",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_product(
    product_request: ProductRequest,

    db: Session = Depends(get_db),

    current_user: models.Users = Depends(
        get_current_user
    )
):

    product = models.Products(
        name=product_request.name,
        description=product_request.description,
        price=product_request.price,
        stock=product_request.stock,
        image_url=product_request.image_url,

        owner_id=current_user.id
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product


# --------------------------------
# UPDATE PRODUCT
# Requires JWT
# --------------------------------

@router.put(
    "/{product_id}",
    response_model=ProductResponse
)
async def update_product(
    product_id: int,
    product_request: ProductRequest,

    db: Session = Depends(get_db),

    current_user: models.Users = Depends(
        get_current_user
    )
):

    product = (
        db.query(models.Products)
        .filter(
            models.Products.id == product_id
        )
        .first()
    )

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    if product.owner_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="You cannot update this product"
        )

    product.name = product_request.name
    product.description = product_request.description
    product.price = product_request.price
    product.stock = product_request.stock
    product.image_url = product_request.image_url

    db.commit()
    db.refresh(product)

    return product


# --------------------------------
# DELETE PRODUCT
# Requires JWT
# --------------------------------

@router.delete(
    "/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_product(
    product_id: int,

    db: Session = Depends(get_db),

    current_user: models.Users = Depends(
        get_current_user
    )
):

    product = (
        db.query(models.Products)
        .filter(
            models.Products.id == product_id
        )
        .first()
    )

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    if product.owner_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="You cannot delete this product"
        )

    db.delete(product)
    db.commit()

    return