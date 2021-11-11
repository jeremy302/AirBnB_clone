#!/usr/bin/python3
''' module for file_storage tests '''
from unittest import TestCase
from unittest.mock import patch
import json
import re
from uuid import UUID, uuid4
from datetime import datetime
from time import sleep
import os
from io import StringIO

from console import HBNBCommand
from models import storage, BaseModel, FileStorage
from models import user
from models.user import User


def clio(sio):
    ''' clears a string i/o buffer '''
    sio.seek(0)
    sio.truncate(0)


class TestHBNBCommand(TestCase):
    ''' tests HBNBCommand class '''
    def test_6(self):
        ''' task 6 test '''
        FS_dict = FileStorage.__dict__
        FS__path = '_FileStorage__file_path'
        FS__objs = '_FileStorage__objects'
        FS_path = FS_dict[FS__path]
        FS_objs = FS_dict[FS__objs]

        mkapp = lambda: HBNBCommand()
        mkbuf = lambda: StringIO()
        sio = mkbuf()
        with patch('sys.stdout', new=sio) as f:
            app: HBNBCommand = mkapp()

            ## TODO: help, quit and EOF validation
            # help not empty
            app.onecmd("help")
            self.assertTrue(sio.getvalue())

            ## create
            # no arg
            clio(sio)
            app.onecmd("create")
            self.assertEqual(sio.getvalue(), "** class name missing **\n")

            # invalid arg
            clio(sio)
            app.onecmd("create ABC")
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")
            clio(sio)
            # case-sensitivity
            app.onecmd("create basemodel")
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")
            clio(sio)
            app.onecmd("create Basemodel")
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")
            clio(sio)
            app.onecmd("create Base")
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")
            clio(sio)
            app.onecmd("create baseModel")
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")

            # valid arg
            clio(sio)
            objs_k = storage.all().copy()
            app.onecmd("create BaseModel")
            # model creation
            kid = 'BaseModel.{}'.format(sio.getvalue()[:-1])
            self.assertTrue(kid not in objs_k and kid in storage.all()
                            and type(storage.all()[kid]) == BaseModel)
            # saved to file
            with open(FS_path, 'r') as file:
                tmp = json.load(file)
                self.assertTrue(type(tmp) is dict and kid in tmp)
            obj = storage.all()[kid]
            storage.all().clear()
            storage.reload()
            self.assertTrue(kid in storage.all())
            self.assertEqual(obj.to_dict(), storage.all()[kid].to_dict())

            ##
            ##
            ##
            ##
            # show
            clio(sio)
            app.onecmd("show")

    def test_8(self):
        '''tests for task 8 in console app and User class'''
        console = HBNBCommand()
        buf = StringIO()

        with patch('sys.stdout', new=buf) as f:
            # test [ create ] command with User class
            console.onecmd('create User')
            user_id = buf.getvalue().strip()
            self.assertTrue(user_id)
            clio(buf)

            # test [ show ] command with the last User created
            console.onecmd('show User ' + user_id)
            self.assertTrue(('[User] (' + user_id + ')') in buf.getvalue())
            clio(buf)

            # test [ all ] command with User class
            console.onecmd('all User')
            self.assertTrue(('[User] (' + user_id + ')') in buf.getvalue())
            clio(buf)

            # test [ update ] command in the last user created with comma seperated args
            console.onecmd('update User ' + user_id + ' first_name updatedName')
            console.onecmd('show User ' + user_id)
            self.assertTrue("'first_name': 'updatedName'" in buf.getvalue())
            clio(buf)

            # test [ destroy ] command to destroy last created User
            console.onecmd('destroy User ' + user_id)
            self.assertEqual(buf.getvalue(), "")
            console.onecmd('show User ' + user_id)
            self.assertEqual(buf.getvalue(), "** no instance found **\n")
            clio(buf)
