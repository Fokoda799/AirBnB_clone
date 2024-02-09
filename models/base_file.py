#!/usr/bin/env python3
"""Base File"""
import uuid
from datetime import *


class Base:
    """Base Class"""

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        print(f"[{self.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        print(__dict__)
test = Base()
test.to_dict
