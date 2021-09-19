from pydantic import BaseModel
from datetime import datetime


class PostSchema(BaseModel):
    title: str
    body: str
