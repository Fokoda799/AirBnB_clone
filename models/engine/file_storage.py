#!/usr/bin/python3
"""File Storage Model"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
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
        for key in FileStorage.__objects:
            dicts[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(dicts, file, indent=2)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                dicts = json.load(file)
            for key in dicts:
                class_name, obj_id = key.split('.')
                if class_name == "BaseModel":
                    FileStorage.__objects[key] = BaseModel(**dicts[key])
                elif class_name == "User":
                    FileStorage.__objects[key] = User(**dicts[key])
                elif class_name == "State":
                    FileStorage.__objects[key] = State(**dicts[key])
                elif class_name == "City":
                    FileStorage.__objects[key] = City(**dicts[key])
                elif class_name == "Amenity":
                    FileStorage.__objects[key] = Amenity(**dicts[key])
                elif class_name == "Place":
                    FileStorage.__objects[key] = Place(**dicts[key])
                elif class_name == "Review":
                    FileStorage.__objects[key] = Review(**dicts[key])
