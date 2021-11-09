#!/usr/bin/python3
''' module for Review class '''
from .base_model import BaseModel


class Review(BaseModel):
    place_id = ''
    user_id = ''
    text = ''
