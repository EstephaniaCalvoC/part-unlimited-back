import pytest

from app.analytics.part import add_words


@pytest.fixture
def DBClient_mock(mocker):
    mock = mocker.patch("app.analytics.part.DBClient", autospec=True)
    return mock


@pytest.fixture
def wound_mock(mocker):
    mock = mocker.MagicMock()
    mock.id = "wound"
    mock.count = 4
    return mock


def test_add_words(DBClient_mock):
    description = "Tightly wound nickel-gravy alloy spring."
    DBClient_mock.get_by_id.return_value = None

    add_words(DBClient_mock, description)

    DBClient_mock.create.assert_called()
    assert DBClient_mock.create.call_count == 6


def test_add_words_duplicate(DBClient_mock, wound_mock):
    description = "Tightly wound"
    DBClient_mock.get_by_id.side_effect = [None, wound_mock]

    add_words(DBClient_mock, description)

    DBClient_mock.create.assert_called_once()
    DBClient_mock.update.assert_called_once()
