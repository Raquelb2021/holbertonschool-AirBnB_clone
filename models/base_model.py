#!/usr/bin/python3
"""Class BaseModel"""

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
        if kwargs:  # Checks if kwargs is provided (i.e., is not empty).
            for key, value in kwargs.items():  # Iterates over each key-value pair in kwargs.
                if key == 'created_at' or key == 'updated_at':  # If the key is 'created_at' or 'updated_at', the value is expected to be a string representing a datetime.
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f') # Converts the string to a datetime object.
                if key != '__class__': # If the key is not '__class__', the value is set as an attribute of the instance.
                    setattr(self, key, value) # Sets the attribute of the instance.
        else:
            self.id = str(uuid.uuid4())  # This code runs if kwargs is not provided or is empty.
            self.created_at = self.updated_at = datetime.now()  # Sets the 'id' attribute to a new, random UUID.
            models.storage.new(self)  # Calls the 'new' method of the 'storage' attribute of the 'models' module, passing in this instance.

    def __str__(self):
        """returns a string representation of the object.

        In the case of the BaseModel class

        """
        return '[{}] ({}) {}'.format(
                self.__class__.__name__,
                self.id,
                self.__dict__
                )   # Returns a string representation of the instance, including the class name, id, and dictionary of attributes.

    def save(self):
        """save(self): updates the public instance
        attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now() # Updating the 'updated_at' timestamp.
        models.storage.save()   # Saving the instance

    def to_dict(self):
        """The to_dict method returns a dictionary
        containing all keys/values of the instance's
        """
        new_dict = self.__dict__.copy()  # Creating a copy of the instance's dictionary.
        new_dict['__class__'] = self.__class__.__name__  # Adding the class name under the '__class__' key.
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat() # Converting 'created_at' and 'updated_at' to string format for JSON serialization.
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict     # Return the new dictionary.

    @classmethod
    def from_dict(cls, obj_dict):
        class_name = obj_dict.get('__class__')
        if class_name:
            class_ = models.classes[class_name]
            obj = class_(**obj_dict)    # Creating an instance of the class using the dictionary.
            return obj
        else:
            raise ValueError("Missing '__class__' key in dictionary.")  # If '__class__' key is not in the dictionary, raise an error.
