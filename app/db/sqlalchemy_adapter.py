import os
from functools import lru_cache

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


@lru_cache(maxsize=1)
def get_engine():
    database_url = os.getenv("DATABASE_URL")
    engine = create_engine(database_url, connect_args={"check_same_thread": False})
    return engine


@lru_cache(maxsize=1)
def get_session():
    engine = get_engine()
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal()


def init_db():
    engine = get_engine()
    Base.metadata.create_all(bind=engine)
