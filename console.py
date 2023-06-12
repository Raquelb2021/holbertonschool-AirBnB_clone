#!/usr/bin/python3
<<<<<<< HEAD
"""Module for Console 0.0.1, 0.1, 1.0 """
=======
<<<<<<< HEAD
"""Module 6. Console 0.0.1"""
=======
"""Module for Console 0.0.1, 0.1, 1.0"""
>>>>>>> 35b36262a0b56d345dbdfb1292db1928fd9b97ee

>>>>>>> efb34717001232edd078981702e727fb2c2573b7
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

<<<<<<< HEAD

class HBNBCommand(cmd.Cmd):
=======
<<<<<<< HEAD
class HBNBcommand(cmd.cmd):
=======
class HBNBcommand(cmd.Cmd):
>>>>>>> efb34717001232edd078981702e727fb2c2573b7
>>>>>>> 35b36262a0b56d345dbdfb1292db1928fd9b97ee
    """Class HBNBCommand inherits from cmd.Cmd and defines methods for our command-line application"""

    prompt = '(hbnb) '  # Custom prompt attribute

    def __init__(self):
        super().__init__()

<<<<<<< HEAD
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit command to exit the program"""
        return True
=======
<<<<<<< HEAD
def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

def do_EOF(self, arg):
=======
def do_quit(self, line):
        """Quit command to exit the program"""
        return True

def do_EOF(self, line):
>>>>>>> efb34717001232edd078981702e727fb2c2573b7
    """Exit command"""
    return True
>>>>>>> 35b36262a0b56d345dbdfb1292db1928fd9b97ee

    def emptyline(self):
        """Do nothing on empty input"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file), and prints the ID."""
        args = shlex.split(arg)  # Split the argument string into a list of individual arguments
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()  # Create a new instance of BaseModel
            new_instance.save()  # Save the new instance to the JSON file
            print(new_instance.id)  # Print the ID of the new instance

<<<<<<< HEAD
    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and ID."""
        args = shlex.split(arg)  # Split the argument string into a list of individual arguments
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance ID missing **")
=======
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
<<<<<<< HEAD
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
=======
>>>>>>> 35b36262a0b56d345dbdfb1292db1928fd9b97ee
        else:
            instance = storage.get("BaseModel", args[1])  # Get the instance based on class name and ID
            if not instance:
                print("** no instance found **")
            else:
                print(instance)  # Print the string representation of the instance

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and ID."""
        args = shlex.split(arg)  # Split the argument string into a list of individual arguments
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance ID missing **")
        else:
            if not storage.delete("BaseModel", args[1]):
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all instances of a class, or all instances if no class name is provided."""
        args = shlex.split(arg)  # Split the argument string into a list of individual arguments
        if len(args) > 0 and args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            instances = storage.all("BaseModel" if len(args) > 0 else None)  # Get all instances of a class
            for instance in instances.values():
                print(instance)  # Print each instance

    def do_update(self, arg):
        """Updates an instance based on the class name and ID by adding or updating an attribute."""
        args = shlex.split(arg)  # Split the argument string into a list of individual arguments
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance ID missing **")
        else:
            instance = storage.get("BaseModel", args[1])  # Get the instance based on class name and ID
            if not instance:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                setattr(instance, args[2], args[3])  # Set the attribute of the instance
                instance.save()  # Save the updated instance


if __name__ == '__main__':
<<<<<<< HEAD
    HBNBCommand().cmdloop()  # Start the command-line interface loop
=======
    HBNBcommand().cmdloop()  # Start the command-line interface loop
>>>>>>> efb34717001232edd078981702e727fb2c2573b7
>>>>>>> 35b36262a0b56d345dbdfb1292db1928fd9b97ee
