from pydantic import BaseModel
from uuid import UUID

class CreateProductSchema(BaseModel):
    store_id: UUID = None
    name: str
    price: float
    tax_rate: float