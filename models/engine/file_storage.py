import json


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists).
        """
        try:
            with open(FileStorage.__file_path, "r") as file:
                serialized_objects = json.load(file)

            for key, value in serialized_objects.items():
                class_name, obj_id = key.split(".")
                module_name = class_name.lower()
                module = __import__("models." + module_name, fromlist=[class_name])
                cls = getattr(module, class_name)
                obj = cls(**value)
                FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass