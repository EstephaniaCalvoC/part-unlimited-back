"""Pydantic schemas for parts entity"""

from pydantic import BaseModel


class Part(BaseModel):
    id: int
    name: str
    sku: str
    description: str
    weight_ounces: int
    is_active: bool

    class Config:
        from_attributes = True
