import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.session import DBClient
from tests.common import DATABASE_FILE, DATABASE_URL
from tests.integration.helpers import Base


def get_session():
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal()


@pytest.fixture(scope="session", autouse=True)
def environment_variables():
    os.environ["DATABASE_URL"] = DATABASE_URL
    yield
    del os.environ["DATABASE_URL"]


@pytest.fixture(scope="module")
def db_session():
    session = get_session()
    yield session

    session.close()

    if os.path.exists(DATABASE_FILE):
        os.remove(DATABASE_FILE)


@pytest.fixture(scope="module")
def db_client_mock(db_session):
    yield DBClient(db_session)
