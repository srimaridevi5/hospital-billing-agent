from pydantic import BaseModel


class ChatRequest(BaseModel):
    question: str
    patient_name: str


class ChatResponse(BaseModel):
    answer: str