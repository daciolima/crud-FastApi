from pydantic import BaseModel
from datetime import date


class PostSchema(BaseModel):
    title: str
    body: str
    user_id: int


class ShowPostsSchema(BaseModel):
    title: str
    body: str
    created: date
    user_id: int

    class Config:
        orm_mode = True
