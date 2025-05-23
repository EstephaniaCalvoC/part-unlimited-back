from app.crud.part import create_part, delete_part, get_all_parts, get_part_by_id, get_part_by_sku, update_part
from app.schemas.part import Part, PartCreate, PartUpdate
from tests.common import NEW_PART, PART_1, PART_2


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


def test_get_part_by_id(db_client_mock, populate_parts):
    part = get_part_by_id(db_client_mock, PART_1["id"])
    assert Part.model_validate(part).model_dump() == PART_1


def test_get_part_by_id_not_found(db_client_mock):
    part = get_part_by_id(db_client_mock, PART_1["id"])
    assert part is None


def test_delete_part(db_client_mock, populate_parts):
    assert delete_part(db_client_mock, PART_1["id"])


def test_create_part(db_client_mock):
    new_part = create_part(db_client_mock, PartCreate(**NEW_PART))
    assert new_part is not None
    assert 1 == len(get_all_parts(db_client_mock))


def test_update_part(db_client_mock, populate_parts):
    updated_part = update_part(db_client_mock, PART_1["id"], PartUpdate(**{"weight_ounces": 55, "description": None}))
    assert updated_part is not None
    assert updated_part.weight_ounces == 55
    assert updated_part.description is None
