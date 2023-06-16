#!/usr/bin/python3
"""FILE STORAGE MODULE"""
import json
from models.base_model import BaseModel
from datetime import datetime
import models
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User


class FileStorage:
    """STORE NEW FILES"""
    __file_path = "file.json"
    # Private class variable to store the name of the file to which JSON string is written.
    __objects = {}
    # Private class variable to store all objects.

    classes = {
        'BaseModel': BaseModel,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }
    # Class variable to map class names to classes.

    def all(self):
        """
        Returns a dictionary of all objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            obj_dict = {
                    key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(obj_dict, f)

    def reload(self):
        """RELOAD FILES"""
        try:
            with open(self.__file_path, encoding='utf-8') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj

        except FileNotFoundError:
            pass


def from_dict(self, obj_dict):
    # This function converts a dictionary into an object of a given class.
    class_name = obj_dict.get('__class__')
    if class_name:
        class_ = models.classes[class_name]
        obj = class_(**obj_dict)
        return obj
    else:
        raise ValueError("Missing '__class__' key in dictionary.")


def get_instance_by_id(self, class_name, instance_id):
    """Retrieve the instance based on the class name and ID."""
    instances = self.all(class_name)
    for instance in instances.values():
        if instance.id == instance_id:
            return instance
        return None
