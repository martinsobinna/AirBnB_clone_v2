#!/usr/bin/python3
"""The review's class"""
from models.base_model import BaseModel, Base

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String, ForeignKey, Float

from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """The class for the Review
    Attributes:
        place_id: the place's id
        user_id: the user's id
        text: the review's description
    """
    __tablename__ = "reviews"
    text = Column(String(1024),
            nullable=False)
    place_id = Column(String(60),
            ForeignKey("places.id"),
            nullable=False)
    user_id = Column(String(60),
            ForeignKey("users.id"),
            nullable=False)
