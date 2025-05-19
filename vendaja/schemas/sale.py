from pydantic import BaseModel, Field
from datetime import datetime

class CreateSaleModel(BaseModel):
    product_id: int
    customer_phone: str
    customer_name: str = None
    created_at: datetime = Field(default_factory=datetime.now)