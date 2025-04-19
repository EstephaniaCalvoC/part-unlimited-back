from functools import lru_cache
from typing import List, Optional, Tuple

from pydantic import BaseModel, Field, field_validator


@lru_cache(maxsize=128)
def get_lower_words(skip: Tuple[str]):
    return [word.lower() for word in skip]


class RequestWordFrequencyUpdate(BaseModel):
    count: int


class RequestWordFrequency(BaseModel):
    limit: Optional[int] = Field(5, description="Limit of words to return")
    skip: Optional[List] = Field(None, description="List of words to skip")

    @field_validator("skip", mode="before")
    def validate_skip(cls, skip: Optional[List[str]]):
        return get_lower_words(tuple(sorted(skip))) if skip else None

    class Config:
        json_schema_extra = {
            "examples": [
                {"limit": 5, "skip": ["to", "and", "of"]},
                {
                    "limit": 100,
                },
            ]
        }


class ResponseWordFrequency(BaseModel):
    id: str = Field(..., description="Word")
    count: int = Field(..., description="Count of word")

    class Config:
        from_attributes = True
        json_schema_extra = {"examples": [[{"id": "iron", "count": 1}, {"id": "provide", "count": 35}]]}
