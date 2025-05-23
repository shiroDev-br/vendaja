from pydantic import BaseModel, Field
from datetime import datetime

class CreateProductSchema(BaseModel):
    name: str
    price: float
    tax_rate: float
    created_at: datetime = Field(default_factory=datetime.now)