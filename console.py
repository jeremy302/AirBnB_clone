#!/usr/bin/python3
''' module for console '''
from cmd import Cmd
import re
from ast import literal_eval
from models import storage, models

def parse_args(ln):
    ''' parses command arguments '''
    args = []
    arg = ''
    i = 0
    ln_len = len(ln)
    dq = False
    ln.strip()
    while i < ln_len:
        if ln[i] == '"':
            if dq:
                args.append(arg)
                arg = ''
                dq = False
            else:
                dq = True
        elif dq:
            arg += ln[i]
        elif ln[i] not in ' \t\n\f\v':
            arg += ln[i]
        elif arg:
            args.append(arg)
            arg = ''
        i += 1
    if arg or dq:
        args.append(arg)
        arg = ''
    return args

def parse_inf_args(ln):
    ''' parses infix notation command arguments '''
    return literal_eval(ln)

class HBNBCommand(Cmd):
    ''' class for the console '''
    __clss = models

    def emptyline(self):
        pass

    def do_quit(self, arg):
        ''' Quit command to exit the program '''
        return True

    def do_EOF(self, arg):
        ''' EOF command to exit the program '''
        return True

    def do_help(self, arg):
        ''' help command to get help for a command '''
        super().do_help(arg)

    def do_create(self, arg):
        ''' create command to create a new model '''
        clss = type(self).__clss
        args = parse_args(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in clss:
            print("** class doesn't exist **")
        else:
            obj = clss[args[0]]()
            storage.save()
            print(obj.id)

    def do_show(self, arg):
        ''' prints string representation of an instance '''
        clss = type(self).__clss
        args = parse_args(arg)
        key = '.'.join(args[:2])
        if not args:
            print("** class name missing **")
        elif args[0] not in clss:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif key not in storage.all():
            print('** no instance found **')
        else:
            print(storage.all()[key])

    def do_destroy(self, arg):
        ''' deletes an instance '''
        clss = type(self).__clss
        args = parse_args(arg)
        key = '.'.join(args[:2])
        if not args:
            print("** class name missing **")
        elif args[0] not in clss:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif key not in storage.all():
            print('** no instance found **')
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        ''' prints all instances of a class '''
        clss = type(self).__clss
        args = parse_args(arg)
        objs = []

        if not args:
            objs = storage.all().values()
        elif args[0] not in clss:
             print("** class doesn't exist **")
             return
        else:
            objs = [obj for obj in storage.all().values()
                    if type(obj).__name__ == args[0]]

        print(["[{}] ({}) {}".format(
            type(obj).__name__, obj.id,
            {k:v for k, v in obj.to_dict().items() if k != '__class__'})
                for obj in objs])

    def do_update(self, arg):
        ''' updates and instance attribute '''
        clss = type(self).__clss
        args = parse_args(arg)
        key = '.'.join(args[:2])
        if not args:
            print("** class name missing **")
        elif args[0] not in clss:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif key not in storage.all():
            print('** no instance found **')
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            obj = storage.all()[key]
            setattr(obj, args[2], type(getattr(obj, args[2], ''))(args[3]))
            storage.save()

    def _do_all(self, cls, arg):
        ''' prints all instances of a model '''
        self.do_all(cls.__name__)

    def _do_count(self, cls, arg):
        ''' `counts all instances of a model '''
        print(len([v for v in storage.all().values() if type(v) is cls]))

    def _do_show(self, cls, arg):
        ''' prints an instance '''
        self.do_show('{} {}'.format(cls.__name__, arg))

    def _do_destroy(self, cls, arg):
        ''' deletes an instance '''
        self.do_destroy('{} {}'.format(cls.__name__, arg))

    def _do_update(self, cls, arg):
        ''' updates an instance '''
        args = parse_inf_args(arg)
        if len(args) == 3:
            self.do_update('{} {} {} {}'.format(
                cls.__name__, args[0], args[1], args[2]))
        elif len(args) == 2:
            key = '.'.join([cls.__name__, args[0]])
            if key not in storage.all():
                print('** no instance found **')
            else:
                obj = storage.all()[key]
                for k, v in args[1].items():
                    setattr(obj, k, v)
                storage.save()

    def precmd(self, ln):
        ''' processes line to handle infix commands '''
        inf_cmds = {
            'all': self._do_all,
            'count': self._do_count,
            'show': self._do_show,
            'destroy': self._do_destroy,
            'update': self._do_update
        }
        rgx = re.compile(r'(?P<class>{})\.(?P<method>{})\((?P<arg>.*)\)'.format(
            '|'.join(type(self).__clss.keys()), '|'.join(inf_cmds.keys())))
        res = rgx.match(ln)
        if res:
            dct = res.groupdict()
            inf_cmds[dct['method']](type(self).__clss[dct['class']], dct['arg'])
            return ""
        return ln

if __name__ == '__main__':
    HBNBCommand().cmdloop()
