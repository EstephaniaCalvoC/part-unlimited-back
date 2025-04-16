from app.crud.part import get_all_parts
from app.schemas.part import Part
from tests.common import PART_1, PART_2


def test_get_all_parts(db_client_mock, populate_parts):

    results = get_all_parts(db_client_mock)

    assert len(results) == 2
    assert Part.model_validate(results[0]).model_dump() == PART_1
    assert Part.model_validate(results[1]).model_dump() == PART_2


def test_get_all_parts_empty_table(db_client_mock):

    results = get_all_parts(db_client_mock)

    assert len(results) == 0
