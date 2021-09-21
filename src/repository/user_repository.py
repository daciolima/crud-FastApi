from fastapi import status, HTTPException
from src.models import User
from sqlalchemy.orm import Session
from src.schemas import UserSchema, ShowUsersSchema
from src.security import Hash


def users_all(db: Session):
    users = db.query(User).all()
    return users


def user_id(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nenhum usuário encontrado com o id {id}.")
    return user


def create_user(user, db: Session):
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


def update_user(id: int, user, db: Session):
    result = db.query(User).filter(User.id == id)
    if not result.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nenhum post encontrado com o id {id}.")
    result.update({'name': user.name, 'username': user.username, 'email': user.email, 'password': Hash.bcrypt(user.password)})
    db.commit()
    return {"message": f"Usuário id {id} alterado com sucesso."}, {"data": user}


def delete_user(id: int, db: Session):
    user = db.query(User).filter(User.id == id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nenhum usuário encontrado com o id {id}.")

    user.delete(synchronize_session=False)
    db.commit()
    return {"data": f"Usuário excluido com sucesso"}