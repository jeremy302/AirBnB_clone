#!/usr/bin/python3
''' module for User class '''
from .base_model import BaseModel


class User(BaseModel):
    email = ''
    password = ''
    first_name = ''
    last_name = ''
    
