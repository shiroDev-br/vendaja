from pydantic import BaseModel, Field
from datetime import datetime

class CreateStoreSchema(BaseModel):
    name: str
    document: str
    email: str
    phone: str
    created_at: datetime = Field(default_factory=datetime.now)