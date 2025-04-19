# CRUD logic for parts

import logging

from app.analytics.part import add_words, subtract_words
from app.db.models.part import Part
from app.db.session import DBClient
from app.schemas.part import PartCreate, PartUpdate

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
        subtract_words(db, part)
        result = db.delete(part, save=False)
        db.save_changes()
        return result
    except Exception as e:
        logger.error(f"Error deleting part with id {part_id}: {e}")
        raise


def create_part(db: DBClient, part: PartCreate):
    logger.info(f"Creating part: {part}")
    try:
        part = db.create(Part(**part.model_dump()), save=False)
        add_words(db, part.description)
        db.save_changes()
        return part
    except Exception as e:
        logger.error(f"Error creating part: {e}")
        raise


def update_part(db: DBClient, part_id: int, new_data: PartUpdate):
    logger.info(f"Updating part with id: {part_id}")

    part = get_part_by_id(db, part_id)
    if part is None:
        return None

    try:
        new_data_dict = new_data.model_dump(exclude_unset=True)

        description = new_data_dict.get("description", "")

        if description is None:
            subtract_words(db, part)

        if description:
            subtract_words(db, part)
            add_words(db, description)

        result = db.update(part, new_data_dict, save=False)
        db.save_changes()
        return result

    except Exception as e:
        logger.error(f"Error updating part with id {part_id}: {e}")
        raise
