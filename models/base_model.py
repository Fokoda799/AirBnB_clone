#!/usr/bin/python3
"""Base Model"""
from datetime import datetime
import uuid


class BaseModel:
    """Base class"""
    def __init__(self):
        """Iinit fonuction"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Str function"""
        return f"[{BaseModel.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Save function"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """To_dict function"""
        d = {}
        for key in self.__dict__.keys():
            if key in ['created_at', 'updated_at']:
                d[key] = self.__dict__[key].isoformat()
                continue
            d[key] = self.__dict__[key]
        d['__class__'] = self.__class__.__name__
        return d
