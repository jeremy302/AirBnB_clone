#!/usr/bin/python3
'''this module for the console app'''


import cmd
import sys
from models.__init__ import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review



class HBNBCommand(cmd.Cmd):
    '''HBNB Command Prompt class'''

    # determines prompt for interactive/non-interactive modes
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''
    # available classes that can be created
    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }

    attr_types = {
             'number_rooms': int, 'number_bathrooms': int,
             'max_guest': int, 'price_by_night': int,
             'latitude': float, 'longitude': float
            }

    def do_quit(self, arg):
        '''method for the quit command'''
        exit()

    def help_quit(self):
        '''prints the documentation for the command quit'''
        print("The quit command exits the program\n")

    def do_EOF(self, arg):
        '''method that handles the EOF and exit the program'''
        print()
        exit()

    def help_EOF(self):
        """ Prints the documentation for EOF """
        print("The EOF exits the program\n")

    def do_create(self, arg):
        ''' creates a new instance of the class passed as argument
            and saves it to the json storage file
        '''
        if not arg:
            print("** class name missing **")
            return
        elif arg not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[arg]()
        storage.save()
        print(new_instance.id)

    def do_show(self, arg):
        ''' pritns the string representation of an instance
            based on the class name and id
        '''
        args = arg.split()
        cls = args[0]
        id = args[1]

        if not cls:
            print("** class name missing **")
            return
        elif cls not in self.classes:
            print("** class doesn't exist **")
            return
        elif not id:
            print("** instance id missing **")
            return

        key = cls + '.' + id
        if key not in storage._FileStorage__objects:
            print("** no instance found **")
            return
        print(storage._FileStorage__objects[key])

    def do_destroy(self, arg):
        ''' Deletes an instance based on the class name and id
            and saves the change into the JSON Storage file
        '''
        args = arg.split()
        cls = args[0]
        id = args[1]

        if not cls:
            print("** class name missing **")
            return
        elif cls not in self.classes:
            print("** class doesn't exist **")
            return
        elif not id:
            print("** instance id missing **")
            return
        
        key = cls + '.' + id
        if key not in storage._FileStorage__objects:
            print("** no instance found **")
            return

        del (storage.all()[key])
        storage.save()

    def do_all(self, arg):
        ''' Prints all string representation of all instances
            based or not on the class name.
        '''
        result = []
        all = storage.all()
        if not arg:
            for key in all.keys():
                result.append(all[key].__str__())
            print(result)
            return

        if arg not in all:
            print("** class doesn't exist **")
            return

        for key in all.keys():
            if key.find(arg):
                result.append(all[key].__str__())
        print(result)

    def do_update(self, arg):
        '''  Updates an instance based on the class name
            and id by adding or updating attribute and saves
            the change into the JSON Storage file
        '''
        args = arg.split()
        cls = id = attr = val = ''

        if args[0]:
            cls = args[0]
        else:
            print("** class name missing **")
            return
        if cls not in self.classes:
            print("** class doesn't exist **")
            return
        if args[1]:
            id = args[1]
        else:
            print("** instance id missing **")
            return
        key = cls + '.' + id
        if key not in storage.all():
            print("** no instance found **")
            return
        if args[2]:
            attr = args[2]
        else:
            print("** attribute name missing **")
            return
        if args[3]:
            val = args[3]
        else:
            print("** value missing **")
            return

        obj = storage.all()[key]
        # type cast the value depends on the attribute
        if attr in self.attr_types:
            val = self.attr_types[attr](val)
        new_attr = {attr: val}
        # update the object attributes dictionary
        obj.__dict__.update(new_attr)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
