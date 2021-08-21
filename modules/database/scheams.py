from pydantic import BaseModel

from modules.processes.schemas.response import CurrenLoadingResponseSchema


class InfoSchema(BaseModel):
    method: str
    loading: CurrenLoadingResponseSchema
