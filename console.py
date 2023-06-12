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
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        else:
            try:
                model = eval(args[0])()
                model.save()
                print(model.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        else:
            try:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    key = "{}.{}".format(args[0], args[1])
                    objects = storage.all()
                    if key in objects:
                        print(objects[key])
                    else:
                        print("** no instance found **")
            except NameError:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        else:
            try:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    key = "{}.{}".format(args[0], args[1])
                    objects = storage.all()
                    if key in objects:
                        objects.pop(key)
                        storage.save()
                    else:
                        print("** no instance found **")
            except NameError:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all instances of a class"""
        args = shlex.split(arg)
        try:
            objects = storage.all()
            if len(args) == 0:
                print([str(obj) for obj in objects.values()])
            elif args[0] in ["BaseModel"]:
                print([str(obj) for obj in objects.values() if args[0] in str(obj)])
            else:
                print("** class doesn't exist **")
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        else:
            try:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    key = "{}.{}".format(args[0], args[1])
                    objects = storage.all()
                    if key in objects:
                        if len(args) == 2:
                            print("** attribute name missing **")
                        elif len(args) == 3:
                            print("** value missing **")
                        else:
                            setattr(objects[key], args[2], args[3])
                            objects[key].save()
                    else:
                        print("** no instance found **")
            except NameError:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()