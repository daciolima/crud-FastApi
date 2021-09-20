from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Request as RequestCuston, Response
from src.schemas import UserSchema, ShowUsersSchema
from src.security import Hash
from src.models import User
from sqlalchemy.orm import Session
from config.database import session_db

routes_users = APIRouter(
    tags=["Users"]
)


@routes_users.get('/users/all', status_code=status.HTTP_200_OK, response_model=List[ShowUsersSchema])
def users_all(db: Session = Depends(session_db)):
    users = db.query(User).all()
    return users


@routes_users.get('/users/{id}', status_code=200, response_model=ShowUsersSchema)
async def user_id(id, db: Session = Depends(session_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nenhum usuário encontrado com o id {id}.")
    return user


@routes_users.post('/users', status_code=status.HTTP_201_CREATED, response_model=ShowUsersSchema)
async def create_user(user: UserSchema, db: Session = Depends(session_db)):
    new_user = User(
        name=user.name,
        username=user.username,
        email=user.email,
        password=Hash.bcrypt(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@routes_users.put("/users/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=ShowUsersSchema)
async def update_post(id, user: UserSchema, db: Session = Depends(session_db)):
    result = db.query(User).filter(User.id == id)
    if not result.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nenhum post encontrado com o id {id}.")
    result.update({'name': user.name, 'username': user.username, 'email': user.email, 'password': user.password})
    db.commit()
    return {"message": f"Usuário id {id} alterado com sucesso."}, {"data": user}


@routes_users.delete('/users/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id, db: Session = Depends(session_db)):
    user = db.query(User).filter(User.id == id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nenhum usuário encontrado com o id {id}.")

    user.delete(synchronize_session=False)
    db.commit()
    return {"data": f"Usuário excluido com sucesso"}

