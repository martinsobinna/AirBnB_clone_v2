#!/usr/bin/python3
"""The amenity's class"""
from models.base_model import BaseModel, Base

from sqlalchemy import Column, String

from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """The class for the Amenity
    Attributes:
        name: the inputed name
        place_amenities: 
    """
    __tablename__ = "amenities"
    name = Column(String(128),
            nullable=False)
    place_amenities = relationship("Place",
            secondary="place_amenity",
            viewonly=False)
