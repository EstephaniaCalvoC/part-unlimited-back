"""Pydantic schemas for parts entity"""

from typing import Optional

from pydantic import BaseModel


class PartBase(BaseModel):
    name: str
    sku: str
    description: Optional[str]
    weight_ounces: int
    is_active: bool = True


class Part(PartBase):
    id: int

    class Config:
        from_attributes = True


class PartCreate(PartBase):
    pass


class PartUpdate(BaseModel):
    name: Optional[str] = None
    sku: Optional[str] = None
    description: Optional[str] = None
    weight_ounces: Optional[int] = None
    is_active: Optional[bool] = None
