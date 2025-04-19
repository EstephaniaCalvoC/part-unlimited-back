"""FastAPI app setup"""

from dotenv import load_dotenv
from fastapi import APIRouter, FastAPI

from app.api.analytics_routes import router as analytics_router
from app.api.part_routes import router as parts_router
from app.logging_config import setup_logging

load_dotenv(override=True)

setup_logging()

app = FastAPI(title="Parts Unlimited API", description="API for Parts Unlimited parts", version="0.1.0")

api_router = APIRouter()

api_router.include_router(parts_router, prefix="/parts", tags=["Parts"])
api_router.include_router(analytics_router, prefix="/analytics", tags=["Analytics"])

app.include_router(api_router, prefix="/api")
