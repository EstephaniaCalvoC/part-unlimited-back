# Analytics logic for top common words

import logging
import re
from collections import Counter

from app.db.models.word_frequency import WordFrequency
from app.db.session import DBClient
from app.schemas.analytics import RequestWordFrequencyUpdate

logger = logging.getLogger(__name__)


def count_words(description: str):
    words = re.findall(r"\b\w+\b", description.lower())
    word_counts = Counter(words)
    return word_counts


def add_words(db: DBClient, description: str):
    word_counts = count_words(description)
    for word, count in word_counts.items():
        word_frequency = db.get_by_id(WordFrequency, word)
        if word_frequency is None:
            db.create(WordFrequency(id=word, count=count))
        else:
            db.update(
                word_frequency, RequestWordFrequencyUpdate.model_validate({"count": word_frequency.count + count})
            )
    logger.info(f"Added words from description: {description}")
