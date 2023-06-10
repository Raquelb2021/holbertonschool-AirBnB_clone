#!/usr/bin/python3
import cmd
from models.base_model import BaseModel  # Import the BaseModel class
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "  # Set the prompt for the command line interface

    def emptyline(self):
        """
        Called when an empty line is entered in response to the prompt.
        """
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file),
        and prints the id.
        Usage: create <class_name>
        """
        if not line:
            print("** class name missing **")
            return

        try:
            new_instance = eval(line)()  # Create a new instance of the class specified in the command
            new_instance.save()  # Save the instance to the JSON file
            print(new_instance.id)  # Print the id of the newly created instance
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name and id.
        Usage: show <class_name> <id>
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + "." + args[1]  # Construct the key for the instance in the storage dictionary
        obj = storage.all().get(key)  # Get the instance from the storage dictionary
        if obj is None:
            print("** no instance found **")
        else:
            print(obj)  # Print the string representation of the instance

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        Usage: destroy <class_name> <id>
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + "." + args[1]  # Construct the key for the instance in the storage dictionary
        obj = storage.all().get(key)  # Get the instance from the storage dictionary
        if obj is None:
            print("** no instance found **")
        else:
            del storage.all()[key]  # Delete the instance from the storage dictionary
            storage.save()  # Save the updated storage dictionary to the JSON file

    def do_all(self, line):
        """
        Prints all string representation of all instances based or not on the class name.
        Usage: all or all <class_name>
        """
        args = line.split()
        objs = storage.all()  # Get all instances from the storage dictionary
        if not args:
            print([str(obj) for obj in objs.values()])  # Print string representation of all instances
        elif args[0] in storage.classes:
            print([str(obj) for obj in objs.values() if type(obj).__name__ == args[0]])  # Print string representation of instances of a specific class
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or updating
        an attribute. Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        key = args[0] + "." + args[1]  # Construct the key for the instance in the storage dictionary
        obj = storage.all().get(key)  # Get the instance from the storage dictionary
        if obj is None:
            print("** no instance found **")
        else:
            setattr(obj, args[2], args[3].strip('"'))  # Set the attribute value of the instance
            obj.save()  # Save the updated instance to the JSON file

    def do_quit(self, line):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, line):
        """
        Handles the EOF signal (Ctrl+D) to exit the program.
        """
        return True

    def postloop(self):
        """
        Method called after a command terminates.
        """
        print()

    def precmd(self, line):
        """
        This method is called after the line has been input but before
        it has been interpreted.
        """
        if line and line.split()[0] in ["update"]:
            line = line.replace(",", "")
        return line


if __name__ == "__main__":
    HBNBCommand().cmdloop()
