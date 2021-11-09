#!/usr/bin/python3
''' creates a static FileStorage instance '''
from .engine.file_storage import FileStorage


storage = FileStorage()


from .base_model import BaseModel
from .amenity import Amenity
from .city import City
from .place import Place
from .review import Review
from .state import State
from .user import User


models = {c.__name__: c
          for c in [BaseModel, Amenity, City, Place, Review, State, User]}
storage.reload()
