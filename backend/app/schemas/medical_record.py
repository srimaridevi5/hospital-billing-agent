from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class MedicalRecordCreate(BaseModel):
    patient_id: UUID


class MedicalRecordResponse(BaseModel):
    id: UUID
    patient_id: UUID
    uploaded_file: str
    extracted_json: str | None
    uploaded_at: datetime

    model_config = {
        "from_attributes": True
    }