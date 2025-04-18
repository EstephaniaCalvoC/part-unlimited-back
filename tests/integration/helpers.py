from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PartModel(Base):
    __tablename__ = "part"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(150), nullable=False)
    sku = Column(String(30), nullable=False, unique=True)
    description = Column(String(1024), nullable=True)
    weight_ounces = Column(Integer, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)


class WordFrequencyModel(Base):
    __tablename__ = "word_frequency"
    id = Column(String, primary_key=True, nullable=False)
    count = Column(Integer, nullable=False)
