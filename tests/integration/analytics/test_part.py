from app.analytics.part import add_words, subtract_words
from tests.common import PART_1
from tests.integration.helpers import PartModel, WordFrequencyModel


def test_add_words(db_client_mock):
    description = "Tightly wound nickel-gravy alloy spring."

    add_words(db_client_mock, description)
    db_client_mock.save_changes()

    add_words(db_client_mock, description.capitalize())
    db_client_mock.save_changes()

    add_words(db_client_mock, description.upper())
    db_client_mock.save_changes()

    add_words(db_client_mock, description.lower())
    db_client_mock.save_changes()

    word_frequencies = db_client_mock.get_all(WordFrequencyModel)

    db_client_mock.db.query(WordFrequencyModel).delete()
    db_client_mock.db.commit()

    assert len(word_frequencies) == 6
    assert all([word.count == 4 for word in word_frequencies])


def test_subtract_words(db_client_mock):
    description = "Tightly wound nickel-gravy alloy spring."

    add_words(db_client_mock, description)
    db_client_mock.save_changes()

    subtract_words(db_client_mock, PartModel(**PART_1))
    db_client_mock.save_changes()

    word_frequencies = db_client_mock.get_all(WordFrequencyModel)

    assert len(word_frequencies) == 6
    assert all([word.count == 0 for word in word_frequencies])
