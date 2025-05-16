from pydantic import BaseModel, Field
import uuid

class StoreSchema(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    name: str
    document: str
    email: str
    phone: str