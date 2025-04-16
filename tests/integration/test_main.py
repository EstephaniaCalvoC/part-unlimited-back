from fastapi.testclient import TestClient

from app.db.models.part import Part as PartModel
from app.main import app
from tests.common import PART_1, PART_2

client = TestClient(app)


def test_get_parts(db_session):

    db_session.add(PartModel(**PART_1))
    db_session.add(PartModel(**PART_2))
    db_session.commit()

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
