from pydantic import BaseModel

class LoginSchema(BaseModel):
    name: str
    password: str

