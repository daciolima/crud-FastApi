from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Request as RequestCuston, Response
from src.schemas import UserSchema, ShowUsersSchema
from src.models import User
from sqlalchemy.orm import Session
from config.database import session_db
from src.repository import user_repository

routes_users = APIRouter(
    tags=["Users"]
)


@routes_users.get('/users/all', status_code=status.HTTP_200_OK, response_model=List[ShowUsersSchema])
def users_all(db: Session = Depends(session_db)):
    return user_repository.users_all(db)


@routes_users.get('/users/{id}', status_code=200, response_model=ShowUsersSchema)
async def user_id(id, db: Session = Depends(session_db)):
    return user_repository.user_id(id, db)


@routes_users.post('/users', status_code=status.HTTP_201_CREATED, response_model=ShowUsersSchema)
async def create_user(user: UserSchema, db: Session = Depends(session_db)):
    return user_repository.create_user(user, db)


@routes_users.put("/users/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_user(id, user: UserSchema, db: Session = Depends(session_db)):
    return user_repository.update_user(id, user, db)


@routes_users.delete('/users/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id, db: Session = Depends(session_db)):
    return user_repository.delete_user(id, db)


