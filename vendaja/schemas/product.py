from pydantic import BaseModel, Field
from datetime import datetime
from uuid import uuid

class CreateProductSchema(BaseModel):
    store_id: uuid = None
    name: str
    price: float
    tax_rate: float
    created_at: datetime = Field(default_factory=datetime.now)