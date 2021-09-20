from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base, engine
import datetime


# Create Database
Base.metadata.create_all(engine)


class Post(Base):

    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    body = Column(Text, nullable=False)
    published = Column(Boolean, default=False)
    created = Column(DateTime, default=datetime.datetime.now)
    updated = Column(DateTime, default=datetime.datetime.now)
    user_id = Column(Integer, ForeignKey('users.id'))

    autor = relationship('User', back_populates="posts")


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    created = Column(DateTime, default=datetime.datetime.now)
    updated = Column(DateTime, default=datetime.datetime.now)

    posts = relationship('Post', back_populates="autor")

