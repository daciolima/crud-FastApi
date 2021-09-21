from sqlalchemy.orm import Session
from fastapi import status, HTTPException
from src.models import Post
from src.schemas import PostSchema


def post_all(db: Session):
    posts = db.query(Post).all()
    return posts


def post_id(id: int, db: Session):
    post = db.query(Post).filter(Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nenhum post encontrado com o id {id}.")
    return post


def create_post(post, db: Session):
    new_post = Post(
        title=post.title,
        body=post.body,
        user_id=post.user_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def update_post(id: int, post: PostSchema, db: Session):
    result = db.query(Post).filter(Post.id == id)
    if not result.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nenhum post encontrado com o id {id}.")
    result.update({'title': post.title, 'body': post.body})
    db.commit()
    return {"message": f"Post id {id} alterado com sucesso."}, {"data": post}


def delete_post(id, db: Session):
    post = db.query(Post).filter(Post.id == id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nenhum post encontrado com o id {id}.")

    post.delete(synchronize_session=False)
    db.commit()
    return {"data": f"Post excluido com sucesso"}