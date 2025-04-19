import logging

from app.analytics.part import add_words
from app.db.models.part import Part
from app.db.session import DBClient, get_db

logger = logging.getLogger(__name__)


def migrate_word_frequency(db: DBClient):
    logger.info("Start word frequency migration")
    parts = db.get_all(Part)
    for part in parts:
        add_words(db, part.description)
        db.save_changes()
        logger.info(f"Added words from partion {part.id} description")
    logger.info("End word frequency migration")


if __name__ == "__main__":
    db = next(get_db())
    migrate_word_frequency(db)
