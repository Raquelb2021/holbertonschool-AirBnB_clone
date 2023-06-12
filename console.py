#!/usr/bin/python3
"""Module for Console 0.0.1, 0.1, 1.0"""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """class HBNB inherits from cmd.Cmd"""
    prompt = '(hbnb) '

    def __init__(self):
        """ init method to HBNBcommand subclass of cmd.CMD """
        super().__init__()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty input"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        args = shlex.split(arg) # Split the argument string into a list of individual arguments
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()  # Create a new instance of BaseModel
            new_instance.save()  # Save the new instance to the JSON file
            print(new_instance.id)  # Print the ID of the new instance

    def do_show(self, arg):
        """Prints the string representation of an
        instance"""
        args = shlex.split(arg) # Split the argument string into a list of individual arguments
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            instance = storage.get("BaseModel", args[1])  # Get the instance based on class name and ID
            if not instance:
                print("** no instance found **")
            else:
                print(instance) # Print the string representation of the instance

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = shlex.split(arg)  # Split the argument string into a list of individual arguments
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            if not storage.delete("BaseModel", args[1]):
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all instances of a class"""
        args = shlex.split(arg)  # Split the argument string into a list of individual arguments
        if len(args) > 0 and args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            instances = storage.all("BaseModel" if len(args) > 0 else None) # Get all instances of a class
            for instance in instances.values():
                print(instance) # Print each instance

    def do_update(self, arg):
        """Updates an instance based on the class name"""
        args = shlex.split(arg) # Split the argument string into a list of individual arguments
        if len(args) == 0:
            print("** class name missing **")  # Set the attribute of the instance
        elif args[0] != "BaseModel":
            print() # Save the updated instance


if __name__ == '__main__':
    HBNBCommand().cmdloop()