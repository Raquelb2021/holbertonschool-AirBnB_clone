#!/user/bin/python3
"""File Storage Module"""
import json
import models
from models.base_model import BaseModel

class FileStorage:
    """Store New Files"""
    __file_path = "file.json" # Path to the JSON file
    __objects = {}  # Dictionary to store all objects

def all(self):
    """Return all the files"""
    return self.__objects

def new(self, obj):
    """New object"""
    key = "{}.{}".format(type(obj.__name__, obj.id))
    FileStorage.__objects[key] = obj

def save(self):
    """SAVE FILES"""
    with open(self.__file_path, mode= "w") as f:
        json.dump(self.__objects, f) # Serialize and save the objects to the JSON file

def save(self):
    """Serializes __objects to the JSON file (path: __file_path)"""
    with open(self.__file_path, mode= "w", encoding='utf-8' ) as f:
    # Serialize each object to its dictionary representation
            serialized_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(serialized_objects, f)  # Serialize and save the objects to the JSON file

def reload(self):
        """RELOAD FILES"""
        try:
            with open(self.__file_path, encoding='utf-8') as f:
                loaded_objects = json.load(f)  # Load the objects from the JSON file
                for key, value in loaded_objects.items():
                    class_name = value['__class__']  # Get the class name from the dictionary
                    obj = eval(class_name)(**value)  # Create an instance of the corresponding class using eval
                    self.__objects[key] = obj  # Add the object to the dictionary

        except FileNotFoundError:
            pass  # If the file is not found, ignore and continue execution