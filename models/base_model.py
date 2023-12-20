#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import models
from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime


Base = declarative_base()


class BaseModel:
    """This class is to define all the common attributes or methods
    for the other classes
    """
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instantiation of the base model's class
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for keeyy, valluee in kwargs.items():
                if keeyy == "created_at" or keeyy == "updated_at":
                    valluee = datetime.strptime(valluee, "%Y-%m-%dT%H:%M:%S.%f")
                if keeyy != "__class__" and hasattr(self, keeyy):
                    setattr(self, keeyy, valluee)

    def __str__(self):
        """returning a str
        Return:
            returning a string of  the class id, name, and a dictionary
        """
        clss = self.__dict__.copy()
        clss.pop('_sa_instance_state', None)
        return "[{}] ({}) {}".format(type(self).__name__, self.id, clss)

    def __repr__(self):
        """returning a str representaion
        """
        return self.__str__()

    def save(self):
        """updating the public instance's attribute
        updated_at to be current
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """creating the dictionary of this class and then returns
        Return:
            returning a dictionary thats of all the keeyy
            values in __dict__
        """
        my_dicty = dict(self.__dict__)
        my_dicty["__class__"] = str(type(self).__name__)
        my_dicty["created_at"] = self.created_at.isoformat()
        my_dicty["updated_at"] = self.updated_at.isoformat()
        if '_sa_instance_state' in my_dicty.keys():
            del my_dicty['_sa_instance_state']
        return my_dicty

    def delete(self):
        """ deleting the object
        """
        models.storage.delete(self)
