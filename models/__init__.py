#!/usr/bin/python3
''' creates a static FileStorage instance '''
from .engine.file_storage import FileStorage

storage = FileStorage()
"""unique FileStorage instance
"""
storage.reload()
