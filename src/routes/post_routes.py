from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException, Request as RequestCuston
from sqlalchemy.orm import Session
from src.schemas import PostSchema, ShowPostsSchema
from src.repository import post_repository
from config.database import session_db


routes_posts = APIRouter(
    tags=["Posts"]
)


@routes_posts.get('/blog/all', status_code=status.HTTP_200_OK, response_model=List[ShowPostsSchema])
async def post_all(db: Session = Depends(session_db)):
    return post_repository.post_all(db)


@routes_posts.get('/blog/{id}', status_code=200, response_model=ShowPostsSchema)
async def post_id(id, db: Session = Depends(session_db)):
    return post_repository.post_id(id, db)


@routes_posts.post('/blog', status_code=status.HTTP_201_CREATED, response_model=ShowPostsSchema)
async def create_post(post: PostSchema, db: Session = Depends(session_db)):
    return post_repository.create_post(post, db)


@routes_posts.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_post(id, post: PostSchema, db: Session = Depends(session_db)):
    return post_repository.update_post(id, post, db)


@routes_posts.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id, db: Session = Depends(session_db)):
    return post_repository.delete_post(id, db)


