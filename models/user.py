#!/usr/bin/python3
from models.base_model import BaseModel
"""class user that inherits from BaseModel"""


class User(BaseModel):
    """public class attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
