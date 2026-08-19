import os

from dotenv import load_dotenv


# Load environment variables from .env
load_dotenv()


# -----------------------------
# DATABASE CONFIGURATION
# -----------------------------

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./shopcart.db"
)


# -----------------------------
# JWT CONFIGURATION
# -----------------------------

SECRET_KEY = os.getenv("SECRET_KEY")

ALGORITHM = os.getenv(
    "ALGORITHM",
    "HS256"
)

ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv(
        "ACCESS_TOKEN_EXPIRE_MINUTES",
        "30"
    )
)


# Make sure SECRET_KEY exists
if not SECRET_KEY:
    raise RuntimeError(
        "SECRET_KEY is missing. Add SECRET_KEY to your .env file."
    )