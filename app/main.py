"""FastAPI app setup"""

from dotenv import load_dotenv
from fastapi import APIRouter, FastAPI

from app.api.part_routes import router as parts_router
from app.logging_config import setup_logging

load_dotenv(override=True)

setup_logging()

app = FastAPI()

api_router = APIRouter()

api_router.include_router(parts_router, prefix="/parts", tags=["Parts"])

app.include_router(api_router, prefix="/api")
