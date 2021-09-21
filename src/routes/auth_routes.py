from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from src.schemas import LoginSchema
from config.database import session_db
from src.repository import auth_repository

routes_auth = APIRouter(
    tags=['Auth']
)


@routes_auth.post('/auth')
def login(auth: LoginSchema, db: Session = Depends(session_db)):
    return auth_repository.login(auth, db)

