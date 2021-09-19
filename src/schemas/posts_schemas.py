from pydantic import BaseModel
from datetime import datetime, date


class PostSchema(BaseModel):
    title: str
    body: str


class ShowPostsSchema(BaseModel):
    title: str
    body: str
    created: date

    class Config():
        orm_mode = True
