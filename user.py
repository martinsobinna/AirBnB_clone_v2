#!/usr/bin/python3
"""The user's class"""
from models.place import Place

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String

from models.base_model import BaseModel, Base

from sqlalchemy.orm import relationship

from models.review import Review


class User(BaseModel, Base):
    """The class for the user
    Attributes:
        email: the user's email address
        password: the user's password for you to login to
        first_name: the users first name
        last_name: the user's last name
        place: the relationship to the user-place
        review: 
    """
    __tablename__ = "users"
    email = Column(String(128),
            nullable=False)
    password = Column(String(128),
            nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", cascade="delete",
                          backref="user")
    reviews = relationship("Review", cascade="delete",
                           backref="user")
