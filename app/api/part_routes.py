"""API routes for parts"""

import logging

from fastapi import APIRouter, Depends, HTTPException

from app.crud.part import get_all_parts, get_part_by_sku
from app.db.session import DBClient, get_db
from app.schemas.part import Part as PartSchema

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/", response_model=list[PartSchema])
def get_parts(db: DBClient = Depends(get_db)):
    parts = get_all_parts(db)
    return parts


@router.get("/{sku}", response_model=PartSchema)
def get_part(sku: str, db: DBClient = Depends(get_db)):
    part = get_part_by_sku(db, sku)
    if part is None:
        raise HTTPException(status_code=404, detail="Part not found")
    return part
