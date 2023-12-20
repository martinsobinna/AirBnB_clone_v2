#!/usr/bin/python3
"""This is the city class"""

from models.base_model import BaseModel, Base

from sqlalchemy import ForeignKey

from sqlalchemy import Column, String

from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """The class for the City
    Attributes:
        name: the inputed name
        state_id: The state's id
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60),
            ForeignKey('states.id'),
            nullable=False)
    places = relationship("Place",
            cascade="delete",
            backref="cities")
