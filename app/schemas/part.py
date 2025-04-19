"""Pydantic schemas for parts entity"""

from typing import Optional

from pydantic import BaseModel, Field


class PartBase(BaseModel):
    name: str = Field(..., description="Name of the part")
    sku: str = Field(..., description="SKU of the part")
    description: Optional[str] = Field(None, description="Description of the part")
    weight_ounces: int = Field(..., description="Weight of the part in ounces")
    is_active: bool = Field(True, description="Is the part active?")

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "name": "Part Name",
                    "sku": "SKU123",
                    "description": "Description of the part",
                    "weight_ounces": 100,
                    "is_active": True,
                }
            ]
        }


class Part(PartBase):
    id: int = Field(..., description="ID of the part")

    class Config:
        from_attributes = True
        json_schema_extra = {
            "examples": [
                {
                    "id": 1,
                    "name": "Part Name",
                    "sku": "SKU123",
                    "description": "Description of the part",
                    "weight_ounces": 100,
                    "is_active": True,
                }
            ]
        }


class PartCreate(PartBase):
    pass


class PartUpdate(BaseModel):
    name: Optional[str] = Field(None, description="Name of the part")
    sku: Optional[str] = Field(None, description="SKU of the part")
    description: Optional[str] = Field(None, description="Description of the part")
    weight_ounces: Optional[int] = Field(None, description="Weight of the part in ounces")
    is_active: Optional[bool] = Field(None, description="Is the part active?")

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "name": "Part Name",
                    "sku": "SKU123",
                    "description": "Description of the part",
                    "weight_ounces": 100,
                    "is_active": True,
                },
                {
                    "description": None,
                },
            ]
        }
