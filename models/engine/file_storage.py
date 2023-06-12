#!/usr/bin/python3
"""FILE STORAGE MODULE"""
import json
from models.base_model import BaseModel
from datetime import datetime
import models

class FileStorage:
    """STORE NEW FILES"""
    __file_path = "file.json"
    __objects = {}

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
            obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
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
    class_name = obj_dict.get('__class__')
    if class_name:
        class_ = models.classes[class_name]
        obj = class_(**obj_dict)
        return obj
    else:
        raise ValueError("Missing '__class__' key in dictionary.")

def get(self, class_name, id):
        """Retrieve an instance from the storage by class name and ID"""
        # Load instances from the JSON file
        instances = self.all()

        # Find the instance with the matching class name and ID
        for instance in instances.values():
            if instance.__class__.__name__ == class_name and instance.id == id:
                return instance

        # No instance found with the given class name and ID
        return None