#!/usr/bin/python3
"""File Storage Model"""
from models.base_model import BaseModel
import json
import os


class FileStorage:
    """FileStorage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """All function returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """New fun sets in __objects the obj with key
        <obj class name>.id"""
        FileStorage.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        dicts = {}
        for key in FileStorage.__objects.keys():
            dicts[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(dicts, file, indent=2)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                dicts = json.load(file)
            for key in dicts.keys():
                FileStorage.__objects[key] = BaseModel(**dicts[key])
