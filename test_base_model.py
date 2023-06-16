#!/usr/bin/python3
from models.base_model import BaseModel

# Create an instance of the BaseModel class
my_model = BaseModel()
# Set attributes for the instance
my_model.name = "My First Model"
my_model.my_number = 89
# Print the string representation of the instance
print(my_model)
# Save the instance
my_model.save()
# Print the string representation of the instance after saving
print(my_model)
# Convert the instance to a dictionary
my_model_json = my_model.to_dict()
# Print the JSON representation of the instance
print(my_model_json)
print("JSON of my_model:")
# Iterate over the keys of the JSON dictionary and print their types and values
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
