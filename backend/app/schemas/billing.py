from pydantic import BaseModel
from uuid import UUID


class ServiceCatalogResponse(BaseModel):
    id: UUID
    service_code: str
    service_name: str
    category: str
    unit_price: float

    model_config = {
        "from_attributes": True
    }


class BillItemResponse(BaseModel):
    service_name: str
    quantity: int
    unit_price: float
    total_price: float

    model_config = {
        "from_attributes": True
    }


class BillResponse(BaseModel):
    id: UUID
    subtotal: float
    tax: float
    total: float

    model_config = {
        "from_attributes": True
    }