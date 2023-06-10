#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel


# Reloaded objects
all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

# Create a new object
print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)

# Verify file.json contents after saving the new object
storage.save()

# Reload the objects again
storage.reload()

# Verify reloaded objects
print("-- Reloaded objects after saving and reloading --")
all_objs_reloaded = storage.all()
for obj_id in all_objs_reloaded.keys():
    obj_reloaded = all_objs_reloaded[obj_id]
    obj_created = all_objs[obj_id]
    print(obj_reloaded.id == obj_created.id)

# Verify file.json contents after saving and reloading
print("File contents after saving and reloading:")
with open("file.json", "r") as file:
    print(file.read())
