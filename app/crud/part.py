# CRUD logic for parts

import logging

from app.db.models.part import Part
from app.db.session import DBClient

logger = logging.getLogger(__name__)


def get_all_parts(db: DBClient):
    logger.info("Fetching all parts")

    try:
        return db.get_all(Part)
    except Exception as e:
        logger.error(f"Error fetching all parts: {e}")
        raise


def get_part_by_sku(db: DBClient, part_sku: str):
    logger.info(f"Fetching part with sku: {part_sku}")

    try:
        return db.get_by_unique_field(Part, "sku", part_sku)
    except Exception as e:
        logger.error(f"Error fetching part with sku {part_sku}: {e}")
        raise


def get_part_by_id(db: DBClient, part_id: int):
    logger.info(f"Fetching part with id: {part_id}")

    try:
        return db.get_by_id(Part, part_id)
    except Exception as e:
        logger.error(f"Error fetching part with id {part_id}: {e}")
        raise


def delete_part(db: DBClient, part_id: int):
    logger.info(f"Deleting part with id: {part_id}")
    part = get_part_by_id(db, part_id)
    if part is None:
        return False
    try:
        return db.delete(part)
    except Exception as e:
        logger.error(f"Error deleting part with id {part_id}: {e}")
        raise
