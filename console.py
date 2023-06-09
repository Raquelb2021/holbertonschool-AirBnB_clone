#!/usr/bin/env python3
"""Console module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = '(hbnb) '

    def do_quit(self, _):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, _):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass


def do_create(self,arg):
    """Create a new instance of BaseModel"""
    if not arg:
            print("**class name missing***") #check if class name is provided
    elif arg not in models.classes:
        print("**class doesn't exist**") #check if class exists
    else:
        new_instance = modles.classes[arg]() #create new instance
        new_instance.save()  # Save the instance
        print(new_instance.id)  # Print the ID of the instance


def do_show(self, arg):
    """Prints the string representation of an instance"""
    args = arg.split()
    if not args:
        print("** class name missing **")  # Check if class name is provided
    elif args[0] not in models.classes:
        print("** class doesn't exist **")  # Check if class exists
    elif len(args) < 2:
        print("** instance id missing **")  # Check if instance ID is provided
    else:
        obj_key = args[0] + "." + args[1]
        objects = models.storage.all()
        if obj_key in objects:
            print(objects[obj_key])  # Print the string representation of the instance
        else:
            print("** no instance found **")  # Instance not found


def do_destroy(self, arg):
    """Deletes an instance based on the class name and id"""
    args = arg.split()
    if not args:
        print("** class name missing **")  # Check if class name is provided
    elif args[0] not in models.classes:
        print("** class doesn't exist **")  # Check if class exists
    elif len(args) < 2:
        print("** instance id missing **")  # Check if instance ID is provided
    else:
        obj_key = args[0] + "." + args[1]
        objects = models.storage.all()
        if obj_key in objects:
            del objects[obj_key]  # Delete the instance
            models.storage.save()  # Save the changes
        else:
            print("** no instance found **")  # Instance not found


def do_all(self, arg):
    """Prints all string representations of all instances"""
    objects = models.storage.all()
    if arg:
        if arg not in models.classes:
            print("** class doesn't exist **")  # Check if class exists
            return
        objects = {
            key: obj
            for key, obj in objects.items()
            if obj.__class__.__name__ == arg
        }
    print([str(obj) for obj in objects.values()])  # Print the string representation of all instances


def do_update(self, arg):
    """Updates an instance based on the class name and id"""
    args = arg.split()
    if not args:
        print("** class name missing **")  # Check if class name is provided
    elif args[0] not in models.classes:
        print("** class doesn't exist **")  # Check if class exists
    elif len(args) < 2:
        print("** instance id missing **")  # Check if instance ID is provided
    else:
        obj_key = args[0] + "." + args[1]
        objects = models.storage.all()
        if obj_key not in objects:
            print("** no instance found **")  # Instance not found
        else:
            # Update the instance attribute with the provided value
            setattr(objects[obj_key], args[2], args[3])
            objects[obj_key].save()  # Save the changes

        if __name__ == '__main__':
                HBNBCommand().cmdloop()


