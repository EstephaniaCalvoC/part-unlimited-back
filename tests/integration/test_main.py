import pytest
from fastapi.testclient import TestClient

from app.main import app
from tests.common import PART_1, PART_2
from tests.integration.helpers import PartModel

client = TestClient(app)


@pytest.fixture(scope="function")
def db_with_parts(db_session):
    db_session.add_all([PartModel(**PART_1), PartModel(**PART_2)])
    db_session.commit()
    yield db_session
    db_session.query(PartModel).delete()
    db_session.commit()


def test_get_parts(db_with_parts):

    response = client.get("/api/parts")
    assert response.status_code == 200

    parts = response.json()

    assert len(parts) == 2
    assert parts[0] == PART_1
    assert parts[1] == PART_2


def test_get_parts_empty(db_session):
    response = client.get("/api/parts")
    assert response.status_code == 200

    parts = response.json()

    assert len(parts) == 0


def test_get_part(db_with_parts):
    response = client.get(f"/api/parts/{PART_1['sku']}")

    assert response.status_code == 200

    part = response.json()

    assert part == PART_1


def test_get_part_not_found(db_session):
    response = client.get(f"/api/parts/{PART_1['sku']}")
    assert response.status_code == 404


def test_delete_part(db_with_parts):
    response = client.delete(f"/api/parts/{PART_1['id']}")
    assert response.status_code == 204
    assert db_with_parts.query(PartModel).filter_by(id=PART_1["id"]).first() is None
