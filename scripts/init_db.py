"""Init db for DEV testing"""

from sqlalchemy import Boolean, Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///./parts_unlimited.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()


class Part(Base):
    __tablename__ = "part"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150))
    sku = Column(String(30))
    description = Column(String(1024))
    weight_ounces = Column(Integer)
    is_active = Column(Boolean)


Base.metadata.create_all(bind=engine)
print("✅ SQLite parts table created.")
