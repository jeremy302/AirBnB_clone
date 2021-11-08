#!/usr/bin/python3
'''this module for the console app'''


import cmd
import sys


class HBNBCommand(cmd.Cmd):
    '''HBNB Command Prompt class'''

    # determines prompt for interactive/non-interactive modes
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    def do_quit(self, arg):
        '''method for the quit command'''
        exit()

    def help_quit(self):
        '''prints the documentation for the command quit'''
        print("Exits the program")

    def do_EOF(self, arg):
        '''method that handles the EOF and exit the program'''
        print()
        exit()

    def help_EOF(self):
        """ Prints the documentation for EOF """
        print("Exits the program\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
