from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException, Request as RequestCuston
from src.schemas import PostSchema, ShowPostsSchema
from src.models import Post
from sqlalchemy.orm import Session
from config.database import session_db

routes_custom = APIRouter()


@routes_custom.get('/', status_code=status.HTTP_200_OK)
async def index():
    """ endpoint livros """
    return {"data": {"message": "Blog Index"}}


@routes_custom.get('/blog/all', status_code=status.HTTP_200_OK, response_model=List[ShowPostsSchema])
def post_all(db: Session = Depends(session_db)):
    posts = db.query(Post).all()
    return posts


@routes_custom.get('/blog/{id}', status_code=200, response_model=ShowPostsSchema)
async def post_id(id, db: Session = Depends(session_db)):
    post = db.query(Post).filter(Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nenhum post encontrado com o id {id}.")
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


@routes_custom.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_post(id, post: PostSchema, db: Session = Depends(session_db)):
    result = db.query(Post).filter(Post.id == id)
    if not result.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nenhum post encontrado com o id {id}.")
    result.update({'title': post.title, 'body': post.body})
    db.commit()
    return {"message": f"Post id {id} alterado com sucesso."}, {"data": post}


@routes_custom.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id, db: Session = Depends(session_db)):
    post = db.query(Post).filter(Post.id == id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nenhum post encontrado com o id {id}.")

    post.delete(synchronize_session=False)
    db.commit()
    return {"data": f"Post excluido com sucesso"}

