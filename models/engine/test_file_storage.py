#!/usr/bin/python3

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

# Create an instance of FileStorage
storage = FileStorage()

# Reload objects from file (if file exists)
storage.reload()

# Create a new BaseModel instance
base_model = BaseModel()
base_model.name = "Test Base Model"

# Add the BaseModel instance to the FileStorage
storage.new(base_model)

# Save objects to file
storage.save()

# Clear objects dictionary
storage._FileStorage__objects = {}

# Reload objects from file
storage.reload()

# Access all objects
all_objects = storage.all()

# Print each object
for obj_id, obj in all_objects.items():
    print(obj)

