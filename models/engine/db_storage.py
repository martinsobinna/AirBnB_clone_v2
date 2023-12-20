#!/usr/bin/python3
""" the new class for the sqlAlchemy """
from os import getenv

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker, scoped_session, relationship

from sqlalchemy import (create_engine)

from models.base_model import Base, BaseModel

from models.city import City

from models.state import State

from models.user import User

from models.review import Review

from models.place import Place

from models.amenity import Amenity


class DBStorage:
    """ creating tables thats in the environmental"""
    __engine = None
    __session = None

    def __init__(self):
        userr = getenv("HBNB_MYSQL_USER")
        passwdd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        hostt = getenv("HBNB_MYSQL_HOST")
        envr = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(userr, passwdd, hostt, db),
                                      pool_pre_ping=True)

        if envr == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returning a dictionary
        Return:
            returning the of a dictionary of the __object
        """
        dicty = {}
        if cls:
            objss = self.__session.query(State).all()
            objss.extend(self.__session.query(City).all())
            objss.extend(self.__session.query(User).all())
            objss.extend(self.__session.query(Place).all())
            objss.extend(self.__session.query(Review).all())
            objss.extend(self.__session.query(Amenity).all())

        else:
            if type(cls) == str:
                cls = eval(cls)
            queryy = self.__session.query(cls)
        return {"{}.{}".format(type(x).__name__, x.id): x for x in objss}

    def new(self, obj):
        """adding the new element into the table
        """
        if not self.__session.object_session(obj):
            self.__session.add(obj)
            self.__session.commit()
    def save(self):
        """saving all the changes
        """
        self.__session.commit()
    
    def delete(self, obj=None):
        """deleting just an element thats in the table
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """configurating all
        """
        Base.metadata.create_all(self.__engine)
        secc = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Sessionr = scoped_session(secc)
        self.__session = Sessionr()

    def close(self):
        """ calling the remove() function
        """
        self.__session.close()
