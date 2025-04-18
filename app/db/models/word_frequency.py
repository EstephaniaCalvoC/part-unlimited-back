from sqlalchemy import Column, Integer, String

from app.db.sqlalchemy_adapter import Base


class WordFrequency(Base):
    __tablename__ = "word_frequency"

    id = Column(String, primary_key=True, nullable=False)
    count = Column(Integer, nullable=False)
