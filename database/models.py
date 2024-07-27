
from sqlalchemy import (Column, Integer, Float,
                        String, ForeignKey, DateTime, Boolean)
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    phone_number = Column(String, unique=True)
    user_city = Column(String, default=None, nullable=True)
    password = Column(String)
    reg_date = Column(DateTime)
class PostPhoto(Base):
    #id, post_id, photo_path, reg_date
    __tablename__ = "photo"
    id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(Integer, ForeignKey("post.id"))
    photo_path = Column(String)
    reg_date = Column(DateTime)
    post_fk = relationship("UserPost", lazy="subquery")
class UserPost(Base):
    pass
class Hashtag(Base):
    #id, hashtag_name, post_id, reg_date
    pass
class Comment(Base):
    #id, post_id, user_id, text, reg_date
    pass
