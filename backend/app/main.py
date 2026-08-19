import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import models
from app.database import engine

from app.routers import (
    auth,
    users,
    products,
    categories,
    cart,
    orders,
)


# --------------------------------------------------
# CREATE DATABASE TABLES
# --------------------------------------------------

models.Base.metadata.create_all(bind=engine)


# --------------------------------------------------
# FASTAPI APPLICATION
# --------------------------------------------------

app = FastAPI(
    title="ShopCart API",
    description="Backend API for ShopCart E-commerce Application",
    version="1.0.0",
)


# --------------------------------------------------
# FRONTEND URL
# --------------------------------------------------

FRONTEND_URL = os.getenv("FRONTEND_URL")


# Local development frontends
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:5174",
    "http://127.0.0.1:5174",
]


# Add deployed frontend URL
if FRONTEND_URL:
    origins.append(
        FRONTEND_URL.rstrip("/")
    )


# --------------------------------------------------
# CORS
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# ROUTERS
# --------------------------------------------------

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(products.router)
app.include_router(categories.router)
app.include_router(cart.router)
app.include_router(orders.router)


# --------------------------------------------------
# ROOT
# --------------------------------------------------

@app.get("/")
async def root():
    return {
        "message": "Welcome to ShopCart API"
    }


# --------------------------------------------------
# HEALTH CHECK
# --------------------------------------------------

@app.get("/health")
async def health_check():
    return {
        "status": "Okay"
    }