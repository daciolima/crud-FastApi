from fastapi import APIRouter, Depends, status, Response, HTTPException, Request as RequestCuston
from src.schemas import PostSchema
from src.models import Post
from sqlalchemy.orm import Session
from config.database import session_db

routes_custom = APIRouter()


@routes_custom.get('/', status_code=status.HTTP_200_OK)
async def index():
    """ endpoint livros """
    return {"data": {"message": "Blog Index"}}


@routes_custom.get('/blog/all', status_code=status.HTTP_200_OK)
async def post_all(db: Session = Depends(session_db)):
    posts = db.query(Post).all()
    return posts


@routes_custom.get('/blog/{id}', status_code=200)
async def post_id(id, response: Response, db: Session = Depends(session_db)):
    post = db.query(Post).filter(Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nenhum post encontrado com o id {10}.")
    return post


@routes_custom.post('/blog', status_code=status.HTTP_201_CREATED)
async def create_post(post: PostSchema, db: Session = Depends(session_db)):
    new_post = Post(
        title=post.title,
        body=post.body,
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
