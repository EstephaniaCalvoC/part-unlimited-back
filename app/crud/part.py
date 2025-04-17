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
