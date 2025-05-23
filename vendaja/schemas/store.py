from pydantic import BaseModel

class CreateStoreSchema(BaseModel):
    name: str
    document: str
    email: str
    phone: str