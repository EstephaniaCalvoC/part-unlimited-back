import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock

from app.db.models.part import Part
from app.db.models.word_frequency import WordFrequency
from app.db.session import DBClient
from tests.common import PART_1, PART_2, PARTS_WORDS


@pytest.fixture
def sql_alchemy_session_mock():
    return UnifiedAlchemyMagicMock()


@pytest.fixture
def populate_parts(sql_alchemy_session_mock):

    sql_alchemy_session_mock.add(Part(**PART_1))
    sql_alchemy_session_mock.add(Part(**PART_2))
    sql_alchemy_session_mock.add_all([WordFrequency(**word) for word in PARTS_WORDS])


@pytest.fixture
def db_client_mock(sql_alchemy_session_mock):
    return DBClient(sql_alchemy_session_mock)
