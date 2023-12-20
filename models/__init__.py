#!/usr/bin/python3
"""
Instantiates  that is a storage of object.

-> If the envir variable 'HBNB_TYPE_STORAGE'  that is set to the 'db',
   instantiates the database's storage engine (DBStorage).
-> Otherwise, instantiates (FileStorage).
"""
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
