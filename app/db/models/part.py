# SQLAlchemy model

from sqlalchemy import Boolean, Column, Integer, String

from app.db.sqlalchemy_adapter import Base


class Part(Base):
    print("\n\n###### Part model start")
    __tablename__ = "part"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    sku = Column(String, nullable=False)
    description = Column(String, nullable=False)
    weight_ounces = Column(Integer, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
