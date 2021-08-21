from pydantic import BaseModel


class CurrentLoadingRequestSchema(BaseModel):
    cpu: bool = False
    ram: bool = False


class DeleteRecordingsRequestSchema(BaseModel):
    start: str
    end: str
