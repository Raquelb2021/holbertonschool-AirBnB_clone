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
        key = "{}.{}".format(type(obj).__name__, obj.id)  # The key is a string containing the class name and the id of the object.
        FileStorage.__objects[key] = obj  # The object is stored in the __objects dictionary with its key.

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            obj_dict = {
                    key: obj.to_dict() for key, obj in self.__objects.items()}  # The __objects dictionary is converted to a dictionary that can be serialized to JSON.
            json.dump(obj_dict, f)  # The dictionary is serialized to JSON and written to the file.

    def reload(self):
        """RELOAD FILES"""
        try:
            with open(self.__file_path, encoding='utf-8') as f:
                obj_dict = json.load(f)  # The JSON file is read and deserialized to a dictionary.
                for key, value in obj_dict.items():
                    class_name = value['__class__']  # The class name of the object is extracted from the dictionary.
                    obj = eval(class_name)(**value)  # A new object of the appropriate class is created from the dictionary.
                    self.__objects[key] = obj  # The object is stored in the __objects dictionary.

        except FileNotFoundError:
            pass  # If the file does not exist, nothing is done.


def from_dict(self, obj_dict):
    # This function converts a dictionary into an object of a given class.
    class_name = obj_dict.get('__class__')  # The class name is extracted from the dictionary.
    if class_name:
        class_ = models.classes[class_name]  # The actual class is obtained from the models.classes dictionary.
        obj = class_(**obj_dict)  # A new object is created from the dictionary.
        return obj
    else:
        raise ValueError("Missing '__class__' key in dictionary.")  # If the dictionary does not contain the class name, an exception is raised.


def get_instance_by_id(self, class_name, instance_id):
    """Retrieve the instance based on the class name and ID."""
    instances = self.all(class_name)  # All instances of a specific class are obtained.
    for instance in instances.values():
        if instance.id == instance_id:
            return instance # The instance with the specific id is found and returned.
        return None  # If no instance with the specific id is found, None is returned.
