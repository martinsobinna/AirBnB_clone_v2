#!/usr/bin/python3
"""The state's class"""
import models

from os import getenv

from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base

from sqlalchemy import Column, String

from models.city import City


class State(BaseModel, Base):
    """The class for the State
    Attributes:
        name: the inputed name
        cites: rhe state's city relaton
    """
    __tablename__ = "states"
    name = Column(String(128),
            nullable=False)
    cities = relationship("City", cascade='delete',
            backref="state")

    
    if getenv("HBNB_TYPE_STOAGE") != "db":
        @property
        def cities(self):
            """gettting  a list of all the related city in  the object """
            cityy_listt = []
            for cityy in list(models.storage.all(City).values()):
                if cityy.state_id == self.id:
                    cityy_listt.append(cityy)
            return cityy_listt
