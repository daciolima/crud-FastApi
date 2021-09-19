from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
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

