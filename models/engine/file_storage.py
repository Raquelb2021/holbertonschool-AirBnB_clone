import json
from models.base_model import BaseModel
from datetime import datetime


class FileStorage:
    __file_path = "file.json"  # Path to the JSON file
    __objects = {}  # Dictionary to store all objects

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(key, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file (__file_path)"""
        json_dict = {}
        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(json_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                json_dict = json.load(file)

            for key, value in json_dict.items():
                class_name, obj_id = key.split(".")
                obj_dict = value
                obj_dict["__class__"] = class_name
                for attr, value in obj_dict.items():
                    if attr.endswith("_at"):
                        obj_dict[attr] = datetime.strptime
                        obj = self.from_dict(obj_dict)
                        self.__objects[key] = obj

        except FileNotFoundError:
            pass

def from_dict(self, obj_dict):
    """Converts a dictionary representation of an object back into an instance of the corresponding class"""
    class_name = obj_dict["__class__"]
    del obj_dict["__class__"]
    return globals()[class_name](**obj_dict)
