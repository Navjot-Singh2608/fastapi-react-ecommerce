from pydantic import BaseModel, Field


# -------------------------
# USER SCHEMAS
# -------------------------

class CreateUserRequest(BaseModel):
    username: str = Field(min_length=3)
    email: str
    first_name: str
    last_name: str
    password: str = Field(min_length=6)


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    first_name: str | None
    last_name: str | None
    is_active: bool

    model_config = {
        "from_attributes": True
    }


# -------------------------
# TOKEN SCHEMAS
# -------------------------

class Token(BaseModel):
    access_token: str
    token_type: str


# -------------------------
# PRODUCT SCHEMAS
# -------------------------

class ProductRequest(BaseModel):
    name: str = Field(min_length=2)
    description: str | None = None
    price: float = Field(gt=0)
    stock: int = Field(ge=0)
    image_url: str | None = None


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str | None
    price: float
    stock: int
    image_url: str | None
    is_active: bool
    owner_id: int | None

    model_config = {
        "from_attributes": True
    }