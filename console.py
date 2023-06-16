#!/usr/bin/python3
"""Module for console 0.0.1, 0.1, 1.0"""
import cmd
import shlex
# shlex provides functions to split the input string.
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}
# A dictionary that maps string class names to actual class objects.

class HBNBCommand(cmd.Cmd):
    """class HBNB inherits from cmd.Cmd"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty input"""
        pass

    def print_error_message(self, message):
        """Helper method to print error messages"""
        print("** " + message + " **")

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        args = shlex.split(arg)
        # Splitting the arguments
        if len(args) == 0:
            # If there are no arguments provided, print error message
            self.print_error_message("class name missing")
        elif args[0] not in ("BaseModel"):
            # If the first argument is not "BaseModel", print error message
            self.print_error_message("class doesn't exist")
        else:
            if args[0] == "BaseModel":
                # If the first argument is "BaseModel", create a new instance of BaseModel
                new_instance = BaseModel()
            elif args[0] == "User":
                # If the first argument is "User", create a new instance of User
                new_instance = User()
            new_instance.save()
            # Save the new instance
            print(new_instance.id)
            # Print the id of the new instance
        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)
        # Print the id of the new instance
        if len(arg) < 1: # If the argument is less than 1 character, print error message
            print("** class name missing **")
        elif arg in classes.keys():
            # If the argument matches a key in the classes dictionary, create a new instance of the matching class
            new = classes[arg]()
            new.save()
            print(new.id)
        else:
            # If the argument doesn't match any key in the classes dictionary, print error message
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = shlex.split(arg)
        # If no arguments were provided
        if len(args) == 0:
            # Print error message indicating that the class name is missing
            self.print_error_message("class name missing")
        # If the first argument (the class name) is not one of the listed classes
        elif args[0] not in (
                "BaseModel", "Place", "State", "City", "Amenity", "Review"):
            # Print error message indicating that the class doesn't exist
            self.print_error_message(
                    "class doesn't exist")
        elif len(args) < 2:
                # Print error message indicating that the instance ID is missing
            self.print_error_message("instance id missing")
        else:
            # Save the class name from the first argument
            class_name = args[0]
            # Save the instance ID from the second argument
            instance_id = args[1]
            # Get all instances from the storage
            instances = storage.all()
            # Create the key in the format "ClassName.ID"
            instance_key = "{}.{}".format(class_name, instance_id)
            # Get the instance from the instances dictionary
            instance = instances.get(instance_key)
        # If the instance was found
        if instance:
            # Print the string representation of the instance
            print(instance)
        else:
            self.print_error_message("no instance found")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)  # split the argument string into list
        if len(args) == 0:  # if no arguments, print error message
            self.print_error_message("class name missing")
        elif args[0] not in (
                "BaseModel", "Place", "State", "City", "Amenity", "Review"):  # if first argument is not a valid class name, print error message
            self.print_error_message("class doesn't exist")
        elif len(args) < 2:  # if instance id is not provided, print error message
            self.print_error_message("instance id missing")
        else:  # if both class name and id are present, continue
            instances = storage.all()  # get all instances
            instance_key = "{}.{}".format(args[0], args[1]) # format the instance key
            if instance_key in instances:  # if the instance exists, delete it
                del instances[instance_key]
                storage.save()  # save the changes
            else:  # if the instance does not exist, print error message
                self.print_error_message("no instance found")

    def do_all(self, arg):
        """Prints all instances of a class"""
        args = shlex.split(arg)  # split the argument string into list
        if len(args) > 0 and args[0] not in (
                "BaseModel", "Place", "State", "City", "Amenity", "Review"):  # if there's an argument and it's not a valid class name, print error message
            self.print_error_message("class doesn't exist")
        else:  # if there's no argument or it's a valid class name, continue
            instances = storage.all()  # get all instances
            if len(args) > 0:  # if there's an argument (i.e., a class name), continue
                class_name = args[0]  # get the class name
                instances = {
                    k: v for k, v in instances.items()  # for each instance...
                    if k.split(".")[0] == class_name  # ...if the class name matches the provided class name, include it in the new instances dictionary
                }
            print([str(instance) for instance in instances.values()])  # print all instances (or those of the specified class)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = shlex.split(arg)
        # The next series of checks ensure we have the necessary number of arguments for the function
        if len(args) == 0:
            self.print_error_message("class name missing")
        elif args[0] not in (
                "BaseModel", "Place", "State", "City", "Amenity", "Review"):  # Checking if class exists
            self.print_error_message("class doesn't exist")
        elif len(args) < 2:  # Checking if instance id is provided
            self.print_error_message("instance id missing")
        elif len(args) < 3:  # Checking if attribute name is provided
            self.print_error_message("attribute name missing")
        elif len(args) < 4:  # Checking if attribute value is provided
            self.print_error_message("value missing")
        else:  # If all necessary arguments are provided, continue
            instances = storage.all()  # Get all instances
            instance_key = "{}.{}".format(args[0], args[1])  # Constructing the key
            instance = instances.get(instance_key)
            # If instance is not found, print an error message. Else, continue
            if instance is None:
                self.print_error_message("no instance found")
            else:
                attribute_name = args[2]  # Get attribute name
                attribute_value = args[3]  # Get attribute value
                setattr(instance, attribute_name, attribute_value)  # Set attribute value for the instance
                instance.save()  # Save the instance


if __name__ == '__main__':
    HBNBCommand().cmdloop()
