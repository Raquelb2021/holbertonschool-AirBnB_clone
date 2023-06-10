#!/usr/bin/python3
"""class basemodel"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """Initialization of basemodel class
    that defines all common attributes/methods for other classes:
    """
    def __init__(self, *args, **kwargs):
        """
        uuid.uuid4() generate unique id

        created_at assign with the current datetime
        when an instance is created

        updated_at assign with the current datetime
        when an instance is created and it will be
        updated every time you change your object
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """returns a string representation of the object.

        In the case of the BaseModel class

        """
        return '[{}] ({}) {}'.format(
                self.__class__.__name__,
                self.id,
                self.__dict__
                )

    def save(self):
        """save(self): updates the public instance
        attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """The to_dict method returns a dictionary
        containing all keys/values of the instance’s
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
