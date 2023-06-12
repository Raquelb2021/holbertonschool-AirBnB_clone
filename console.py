#!/usr/bin/python3
"""Module for console 0.0.1, 0.1, 1.0"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


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
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = shlex.split(arg)
        if len(args) == 0:
            self.print_error_message("class name missing")
        elif args[0] not in ("BaseModel"):
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
            instance = storage.get("BaseModel", args[1])
            if instance is None:
                self.print_error_message("no instance found")
            else:
                storage.delete("BaseModel", args[1])
                storage.save()

    def do_all(self, arg):
        """Prints all instances of a class"""
        args = shlex.split(arg)
        if len(args) > 0 and args[0] not in ("BaseModel"):
            self.print_error_message("class doesn't exist")
        else:
            instances = storage.all("BaseModel" if len(args) > 0 else None)
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
            instances = storage.all("BaseModel").get(args[1])
            instance = next((inst for inst in instances.values() if inst.id == args[1]), None)
            if instance is None:
                self.print_error_message("no instance found")
            else:
                attribute_name = args[2]
                attribute_value = args[3]
                setattr(instance, attribute_name, attribute_value)
                instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
