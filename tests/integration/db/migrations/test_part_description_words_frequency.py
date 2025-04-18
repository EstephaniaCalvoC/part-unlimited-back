import pytest

from app.db.migrations.part_description_words_frequency import migrate_word_frequency
from tests.common import NEW_PART, PART_1, PART_2
from tests.integration.helpers import PartModel, WordFrequencyModel


@pytest.fixture(scope="function")
def db_with_parts(db_session):
    db_session.add_all([PartModel(**PART_1), PartModel(**PART_2), PartModel(**NEW_PART)])
    db_session.commit()
    yield db_session
    db_session.query(PartModel).delete()
    db_session.commit()


def test_migrate_word_frequency(db_client_mock, db_with_parts):
    migrate_word_frequency(db_client_mock)

    word_frequencies = db_client_mock.get_all(WordFrequencyModel)

    assert len(word_frequencies) == 16
    assert all([word.count == 1 for word in word_frequencies])
