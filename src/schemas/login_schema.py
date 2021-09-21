from pydantic import BaseModel
from datetime import date


class LoginSchema(BaseModel):
    username: str
    password: str
