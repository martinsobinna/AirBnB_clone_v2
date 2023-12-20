#!/usr/bin/python3
"""This is the place class"""
from models.amenity import Amenity

from models.base_model import BaseModel, Base

from models.review import Review

from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey

from sqlalchemy.orm import relationship

from os import getenv

import models


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """The class for the Place
    Attributes:
        city_id: the city's id
        user_id: the user's id
        name: the named input
        descriptions: the string's of descriptionss
        number_rooms: the number of the room in integer
        number_bathrooms: the number of the bathrooms in integer
        max_guest: the maximum number of guest in integer
        price_by_night:: thte pice for just staying in integer
        latitude: the latitudee thats only in flaot
        longitude: the longitudee thats only in float
        amenity_ids: the list of the Amenity's ids
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    descriptions = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", cascade="delete",
                               backref="place")
    amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False, overlaps="place_amenities")
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        @property
        def reviews(self):
            """ Returning the list of the reviews.id """
            rev_arb = models.storage.all(Review).values()
            rev_listta = []
            for rev_keyy in list(rev_arb):
                if (rev_keyy.place_id == self.id):
                    rev_listta.append(rev_keyy)
            return (rev_listta)

        @property
        def amenities(self):
            """ Returning the list of all the amenity's ids """
            amty_varb = models.storage.all(Amenity).values()
            amty_listta = []
            for amty_keyy in list(amty_varb):
                if (amty_keyy.id in self.amenity_ids):
                    amty_listta.append(amty_keyy)
            return (amty_listta)

        @amenities.setter
        def amenities(self, obj=None):
            """ Appending the amenity's ids to . the attribute """
            if type(obj) == Amenity:
                self.amenity_ids.append(obj.id)
