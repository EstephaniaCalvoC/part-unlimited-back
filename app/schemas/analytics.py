from functools import lru_cache
from typing import List, Optional, Tuple

from pydantic import BaseModel, field_validator


@lru_cache(maxsize=128)
def get_lower_words(skip: Tuple[str]):
    return [word.lower() for word in skip]


class RequestWordFrequencyUpdate(BaseModel):
    count: int


class RequestWordFrequency(BaseModel):
    limit: int
    skip: Optional[List] = None

    @field_validator("skip", mode="before")
    def validate_skip(cls, skip: Optional[List[str]]):
        return get_lower_words(tuple(sorted(skip))) if skip else None


class ResponseWordFrequency(BaseModel):
    id: str
    count: int

    class Config:
        from_attributes = True
