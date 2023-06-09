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


if __name__ == '__main__':
    HBNBCommand().cmdloop()