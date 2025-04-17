from app.crud.part import get_all_parts, get_part_by_sku
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


def test_get_part_by_sku(db_client_mock, populate_parts):
    part = get_part_by_sku(db_client_mock, PART_1["sku"])
    assert Part.model_validate(part).model_dump() == PART_1


def test_get_part_by_sku_not_found(db_client_mock):
    part = get_part_by_sku(db_client_mock, PART_1["sku"])
    assert part is None
