#!/usr/bin/python3
''' module for FileStorage class '''
import json
from os.path import isfile
import models


class FileStorage:
    ''' class for persistent storage '''
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        ''' initializes a storage engine '''
        pass

    def all(self):
        ''' gets all objects '''
        return self.__objects

    def new(self, obj):
        ''' registers a new object '''
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        ''' saves all objects to a file '''
        with open(self.__file_path, 'w') as file:
            r_objs = self.__objects
            objs = {}
            for k in r_objs:
                v = r_objs[k]
                objs[k] = v.to_dict()
            # objs = {k: r_objs[k] if type(r_objs[k]) is dict
            #         else r_objs[k].to_dict() for k in r_objs}
            json.dump(objs, file)

    def reload(self):
        clss = models.models
        if isfile(self.__file_path):
            with open(self.__file_path, 'r') as file:
                js_objs = json.load(file)
                self.__objects.clear()
                # self.__objects = {}
                for k, v in js_objs.items():
                    cls = clss[v['__class__']]
                    self.__objects[k] = cls(**v)
                # self.__objects = {k: clss[v['__class__']](**v)
                #                   for k, v in js_objs.items()}


                
