from pydantic import BaseModel


class RequestWordFrequencyUpdate(BaseModel):
    count: int
