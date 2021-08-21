from typing import Optional

from pydantic import BaseModel


class CurrenLoadingResponseSchema(BaseModel):
    cpu: Optional[float]
    ram: Optional[float]


class MessageResponsetSchema(BaseModel):
    message: str
