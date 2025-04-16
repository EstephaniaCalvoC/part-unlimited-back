"""API routes for parts"""

import logging

from fastapi import APIRouter, Depends

from app.crud.part import get_all_parts
from app.db.session import DBClient, get_db
from app.schemas.part import Part as PartSchema

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/", response_model=list[PartSchema])
def get_parts(db: DBClient = Depends(get_db)):
    parts = get_all_parts(db)
    return parts
