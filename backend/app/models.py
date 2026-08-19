from app.database import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey


class Users(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String,
        unique=True,
        index=True,
        nullable=False
    )

    email = Column(
        String,
        unique=True,
        index=True,
        nullable=False
    )

    first_name = Column(String)

    last_name = Column(String)

    hashed_password = Column(
        String,
        nullable=False
    )

    is_active = Column(
        Boolean,
        default=True
    )


class Products(Base):
    __tablename__ = "products"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    description = Column(String)

    price = Column(
        Float,
        nullable=False
    )

    stock = Column(
        Integer,
        default=0
    )

    image_url = Column(String)

    is_active = Column(
        Boolean,
        default=True
    )

    owner_id = Column(
        Integer,
        ForeignKey("users.id")
    )