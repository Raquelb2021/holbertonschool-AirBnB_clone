#!/usr/bin/python3
"""Module for console 0.0.1, 0.1, 1.0"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
<<<<<<< HEAD
=======
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
>>>>>>> 6e53a032ba4517f56caf880caa04013ca6790f20


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
        if len(args) == 0:
            self.print_error_message("class name missing")
        elif args[0] not in ("BaseModel"):
            self.print_error_message("class doesn't exist")
        else:
<<<<<<< HEAD
            if args[0] == "BaseModel":
                new_instance = BaseModel()
        elif args[0] == "User":
            new_instance = User()
        new_instance.save()
        print(new_instance.id)
=======
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        if len(arg) < 1:
            print("** class name missing **")
        elif arg in classes.keys():
            new = classes[arg]()
            new.save()
            print(new.id)
        else:
            print("** class doesn't exist **")
>>>>>>> 6e53a032ba4517f56caf880caa04013ca6790f20

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = shlex.split(arg)
        if len(args) == 0:
            self.print_error_message("class name missing")
        elif args[0] != "BaseModel":
            self.print_error_message("class doesn't exist")
        elif len(args) < 2:
            self.print_error_message("instance id missing")
        else:
            instances = storage.all()
            instance = instances.get("BaseModel.{}".format(args[1]))
            if instance is None:
                self.print_error_message("no instance found")
            else:
                print(instance)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            self.print_error_message("class name missing")
        elif args[0] not in ("BaseModel"):
            self.print_error_message("class doesn't exist")
        elif len(args) < 2:
            self.print_error_message("instance id missing")
        else:
            instances = storage.all()
            instance_key = "BaseModel.{}".format(args[1])
            instance = instances.get(instance_key)
            if instance is None:
                self.print_error_message("no instance found")
            else:
                class_name = args[0]
                instance_id = args[1]
                class_obj = classes[class_name]
                instances = class_obj.storage.all()
                instances = storage.all()
                instance_key = "BaseModel.{}".format(args[1])
                instance_key = "{}.{}".format(class_name, instance_id)
            if instance_key in instances:
                    del instances[instance_key]
                    storage.save()
                    class_obj.storage.save()

    def do_all(self, arg):
        """Prints all instances of a class"""
        args = shlex.split(arg)
        if len(args) > 0 and args[0] not in ("BaseModel"):
            self.print_error_message("class doesn't exist")
        else:
            instances = storage.all()
            if len(args) > 0:
                instances = {
                        k: v for k, v in instances.items()
                        if k.startswith("BaseModel")}
            print([str(instance) for instance in instances.values()])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            self.print_error_message("class name missing")
        elif args[0] not in ("BaseModel"):
            self.print_error_message("class doesn't exist")
        elif len(args) < 2:
            self.print_error_message("instance id missing")
        elif len(args) < 3:
            self.print_error_message("attribute name missing")
        elif len(args) < 4:
            self.print_error_message("value missing")
        else:
            instances = storage.all()
            instance_key = "BaseModel.{}".format(args[1])
            instance = instances.get(instance_key)
            if instance is None:
                self.print_error_message("no instance found")
            else:
                attribute_name = args[2]
                attribute_value = args[3]
                setattr(instance, attribute_name, attribute_value)
                instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
