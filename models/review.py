#!/usr/bin/python3

from models.base_model import BaseModel
"""classes that inherit from BaseModel"""


class Review(BaseModel):
    """Public class attributes:"""
    place_id = ''
    user_id = ''
    text = ''
