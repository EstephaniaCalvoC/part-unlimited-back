"""API routes for parts"""

import logging

from fastapi import APIRouter, Depends, HTTPException, status

from app.crud.part import create_part as _create_part
from app.crud.part import delete_part as _delete_part
from app.crud.part import get_all_parts, get_part_by_sku
from app.db.custom_exceptions import IntegrityError
from app.db.session import DBClient, get_db
from app.schemas.part import Part as PartSchema
from app.schemas.part import PartCreate as PartSchemaCreate

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


@router.delete("/{_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_part(_id: int, db: DBClient = Depends(get_db)):
    is_deleted = _delete_part(db, _id)
    if not is_deleted:
        raise HTTPException(status_code=404, detail="Part not found")


@router.post("/", response_model=PartSchema, status_code=status.HTTP_201_CREATED)
def create_part(part: PartSchemaCreate, db: DBClient = Depends(get_db)):
    try:
        return _create_part(db, part)
    except IntegrityError as e:
        raise HTTPException(status_code=422, detail="IntegrityError: sku already exists")
