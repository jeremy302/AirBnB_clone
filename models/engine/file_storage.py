#!/usr/bin/python3
''' module for FileStorage class '''
import json
from os.path import isfile
import models
from json import JSONEncoder


class FileStorage:
    ''' class for persistent storage '''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        ''' gets all objects '''
        return self.__objects

    def new(self, obj):
        ''' registers a new object '''
        self.__objects['{}.{}'.format(
            obj.__class__.__name__, obj.id)] = obj

    def save(self):
        ''' saves all objects to a file '''
        with open(self.__file_path, mode='w') as file:
            json_objs = {}
            for key, value in self.__objects.items():
                json_objs[key] = value.to_dict()
            file.write(JSONEncoder().encode(json_objs))

    def reload(self):
        ''' load objects from a file '''
        clss = models.models
        if isfile(self.__file_path):
            with open(self.__file_path, 'r') as file:
                txt = file.read().strip() or '{}'
                js_objs = json.loads(txt)
                obj = {}
                for k, v in js_objs.items():
                    if v.get('__class__', None) in clss:
                        obj[k] = clss[v['__class__']](**v)
                self.__objects = obj
