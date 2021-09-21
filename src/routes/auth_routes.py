from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from src.schemas import LoginSchema
from config.database import session_db
from src.models import User
from src.security.hashing import Hash

routes_auth = APIRouter(
    tags=['Auth']
)


@routes_auth.post('/auth')
def login(auth: LoginSchema, db: Session = Depends(session_db)):
    user = db.query(User).filter(User.username == auth.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Usuário não encontrado.")
    if not Hash.verify(user.password, auth.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Password não está correto.")
    return user
