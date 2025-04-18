from app.analytics.part import add_words
from tests.integration.helpers import WordFrequencyModel


def test_add_words(db_client_mock):
    description = "Tightly wound nickel-gravy alloy spring."

    add_words(db_client_mock, description)
    add_words(db_client_mock, description.capitalize())
    add_words(db_client_mock, description.upper())
    add_words(db_client_mock, description.lower())

    word_frequencies = db_client_mock.get_all(WordFrequencyModel)

    assert len(word_frequencies) == 6
    assert all([word.count == 4 for word in word_frequencies])
