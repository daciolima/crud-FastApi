from typing import List
from pydantic import BaseModel
from .posts_schema import ShowPostsSchema


class UserSchema(BaseModel):
    name: str
    username: str
    email: str
    password: str


class ShowUsersSchema(BaseModel):
    id: int
    name: str
    username: str
    email: str
    posts: List[ShowPostsSchema] = []

    class Config:
        orm_mode = True


class ShowUsersRelationshipSchema(BaseModel):
    id: int
    name: str
    username: str
    email: str

    class Config:
        orm_mode = True
