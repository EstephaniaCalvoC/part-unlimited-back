import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.session import DBClient
from tests.common import DATABASE_FILE, DATABASE_URL
from tests.integration.helpers import Base


@pytest.fixture(scope="session", autouse=True)
def environment_variables():
    os.environ["DATABASE_URL"] = DATABASE_URL
    yield
    del os.environ["DATABASE_URL"]


@pytest.fixture(scope="session")
def db_session():
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()

    yield session

    session.close()
    engine.dispose()

    if os.path.exists(DATABASE_FILE):
        os.remove(DATABASE_FILE)


@pytest.fixture(scope="session")
def db_client_mock(db_session):
    yield DBClient(db_session)
