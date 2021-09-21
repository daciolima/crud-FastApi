from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from src.models import User
from src.security import Hash


def login(auth, db: Session):
    user = db.query(User).filter(User.username == auth.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Usuário não encontrado.")
    if not Hash.verify(user.password, auth.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Password não está correto.")
    return user
