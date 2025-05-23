from pydantic import BaseModel

class CreateStoreSchema(BaseModel):
    name: str
    password: str
    document: str
    email: str
    phone: str