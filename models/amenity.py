#!/usr/bin/python3
"""Amenity Model"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Init Method"""
        super().__init__(*args, **kwargs)
