from pydantic import BaseModel
from uuid import UUID


class PatientCreate(BaseModel):
    patient_number: str
    full_name: str
    age: int
    gender: str


class PatientResponse(BaseModel):
    id: UUID
    patient_number: str
    full_name: str
    age: int
    gender: str

    model_config = {
        "from_attributes": True
    }