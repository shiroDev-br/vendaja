from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID

class CreateProductSchema(BaseModel):
    store_id: UUID | None = None
    name: str
    price: float
    tax_rate: float
    created_at: datetime = Field(default_factory=datetime.now)