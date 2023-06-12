#!/usr/bin/python3
"""module for Console"""
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
    args = shelex.split(arg) #split the argument string
    if len(args) == 0:
        print("** class name missing")
    elif args[0] != "BaseModel":
        print("** class dosen't exist **")
    else:
        new_instance = BaseModel() # Create a new instance of BaseModel
        new_instance.save()  # Save the new instance to the JSON file
    print(new_instance.id)  # Print the ID of the new instance