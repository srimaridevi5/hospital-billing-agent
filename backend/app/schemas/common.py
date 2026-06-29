from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime


class APIResponse(BaseModel):
    success: bool
    message: str


class TimestampSchema(BaseModel):
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class UUIDSchema(BaseModel):
    id: UUID

    model_config = ConfigDict(from_attributes=True)