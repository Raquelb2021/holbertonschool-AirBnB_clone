#!/usr/bin/python3
from models.base_model import BaseModel
# Create an instance of the BaseModel class
my_model = BaseModel()
# Set attributes for the instance
my_model.name = "My_First_Model"
my_model.my_number = 89
# Print the ID of the instance
print(my_model.id)
# Print the string representation of the instance
print(my_model)
# Print the type of the 'created_at' attribute of the instance
print(type(my_model.created_at))
print("--")
# Convert the instance to a dictionary
my_model_json = my_model.to_dict()
# Print the JSON representation of the instance
print(my_model_json)
print("JSON of my_model:")
# Iterate over the keys of the JSON dictionary and print their types and values
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
# Create a new instance of BaseModel using the dictionary
my_new_model = BaseModel(**my_model_json)
# Print the ID of the new instance
print(my_new_model.id)
# Print the string representation of the new instance
print(my_new_model)
# Print the type of the 'created_at' attribute of the new instance
print(type(my_new_model.created_at))

print("--")
# Check if the original instance and the new instance are the same object
print(my_model is my_new_model)
