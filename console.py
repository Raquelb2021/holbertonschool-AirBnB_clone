#!/usr/bin/python3
"""Module 6. Console 0.0.1"""
import cmd
import shlex
from models.base_model import BaseModel  # Import the BaseModel class
from models import storage
from models.engine.file_storage import FileStorage

class HBNBcommand(cmd.cmd):
    """Class HBNBCommand inherits from cmd.Cmd and defines methods for our command-line application"""
    prompt = '(hbnb)'

def __init__(self):
    pass

def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

def do_EOF(self, arg):
    """Exit command"""
    return True

def emptyline(self):
    """Do nothing on empty input"""
    pass

def do_create(self, arg):
    """Creates a new instance of BaseModel"""
    args = shlex.split(arg) #split the argument string
    if len(args) == 0:
        print("** Class Name Missing **")
    elif args[0] != "BaseModel":
        print("** Class Dosen't Exist **")
    else:
        new_instance = BaseModel() # Create a new instance of BaseModel
        new_instance.save()  # Save the new instance to the JSON file
    print(new_instance.id)  # Print the ID of the new instance

def do_show(self, arg):
    """Prints the string representation of an instance based on the class name and ID."""
    args = shlex.split(arg) # Split the argument string into a list of individual arguments
    if len(args) == 0:
        print("** Class Name Missing **")
    elif args[0] != "BaseModel":
        print("** Class Doesn't Exist **")
    elif len(args) < 2:
        print("** Instance Id Missing **")
    else:
        instance = storage.get("BaseModel", args [1]) # Get the instance based on class name and ID
        if not instance:
            print("** No Instance Found **")
        else:
            print(instance) # Print the string representation of the instance

def do_destroy(self, arg):
    """Deletes an instance based on the class name and ID."""
    args = shlex.split(arg)   # Split the argument string into a list of individual arguments
    if len(args) == 0:
        print("** Class Name Missing **")
    elif args[0] != "BaseModel":
        print("** Class Doesn't Exist **")
    elif len(args) < 2:
        print("** Instance ID Missing **")
    else:
        if not storage.delete("Basemodel", args[1]):
            print("** No Instance Found **")

def do_all(self, arg):
    """Prints all instances of a class, or all instances if no class name is provided."""
    args = shlex.split(arg) # Split the argument string into a list of individual arguments
    if len(args) == 0:
        print("** Class Name Missing **")
    elif args[0] != "BaseModel":
        print("** Class Doesn't Exist **")
    else:
        instance = storage.all("BaseModel" if len(args) > 0 else None) # Get all instances of a class
    for instance in instance.values():
        print(instance)

def do_update(self, arg):
    """Updates an instance based on the class name and ID by adding or updating an attribute."""
    args = shlex.split(arg)  # Split the argument string into a list of individual arguments
    if len(args) == 0:
        print("** Class Name Missing **")
    elif args[0] != "BaseModel":
        print("** Class Doesn't Exist **")
    elif len(args) < 2:
        print("** Instance ID Missing **")
    else:
        instance = storage.get("BaseModel", args[1])  # Get the instance based on class name and ID
        if not instance:
            print("** No Instance Found **")
        elif len(args) < 3:
            print("** Attribute Name Missing **")
        elif len(args) < 4:
            print("** Value Missing **")
        else:
            setattr(instance, args[2], args[3]) # Set the attribute of the instance
            instance.save()  # Save the updated instance

    if __name__ == '__main__':
        HBNBcommand().cmdloop()  # Start the command-line interface loop
