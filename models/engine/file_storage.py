#!/usr/bin/python3
"""This class manages the file storage for the hbnb clone"""
import json

from models.base_model import BaseModel

from models.city import City

from models.user import User

from models.state import State

from models.place import Place

from models.review import Review

from models.amenity import Amenity


class FileStorage:
    """This class manages and stores it in JSON format
    Attributes:
        __file_path (str): The directory to the file
        __objects (dict): The obj

    """
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns  storage.

        Args:
            cls (class, optional): If spesult to include
                only cified class.

        Returns:
            dict: A dictionary cin storage.
        """
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            cls_dictt = {}
            for keyy, valuee in self.__objects.items():
                if type(valuee) == (cls):
                    cls_dictt[keyy] = valuee
            return cls_dictt
        return self.__objects

    def new(self, obj):
        """Adds to the storage dictionary new obj"""
        self.__objects["{}.{}".format(type(obj).__name__,  obj.id)] = obj

    def save(self):
        """Saves in the storage dictionary to file"""
        ordict = {o: self.__objects[o].to_dict() for o in self.__objects.keys()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(ordict, f)

    def reload(self):
        """Loads storage dictionary from file."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for x in json.load(f).values():
                    name = x.pop("__class__", None)
                    if name:
                        self.new(eval(name)(**x))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
         Delete obj from __objects ione,
           the method yth shouldn't do anything
        """
        try:
            del self.__objects["{}.{}".format(type(obj).__name__,  obj.id)]
        except (AttributeError, KeyError):
            pass
