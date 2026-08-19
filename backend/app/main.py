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


models.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="ShopCart API",
    description="Backend API for ShopCart E-commerce Application",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174",
        "http://localhost:5174"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.router)
app.include_router(users.router)
app.include_router(products.router)
app.include_router(categories.router)
app.include_router(cart.router)
app.include_router(orders.router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to ShopCart API"
    }


@app.get("/health")
async def health_check():
    return {
        "status": "Okay"
    }