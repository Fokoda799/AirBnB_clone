#!/usr/bin/python3
"""Base Model"""
from datetime import datetime, timedelta
import uuid


class BaseModel:
    """Base class"""

    def __init__(self, *args, **kwargs):
        """Init function"""
        if kwargs:
            for key in kwargs:
                if key in {'created_at', 'updated_at'}:
                    setattr(self, key, datetime.fromisoformat(kwargs[key]))
                elif key == 'id':
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def __str__(self):
        """Str function"""
        ek = {'__class__'}
        od = {k: v for k, v in self.__dict__.items() if k not in ek}
        return f"[{self.__class__.__name__}] ({self.id}) {od}"

    def save(self):
        """Save function"""
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """To_dict function"""
        ek = {'__class__'}
        od = {k: v for k, v in self.__dict__.items() if k not in ek}
        od['created_at'] = od['created_at'].isoformat()
        od['updated_at'] = od['updated_at'].isoformat()
        od['__class__'] = self.__class__.__name__
        for a in dir(self):
            if not callable(getattr(self, a)):
                if not a.startswith("__") and a not in ek:
                    od[a] = getattr(self, a)
        return od
