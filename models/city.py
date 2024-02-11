#!/usr/bin/python3
"""City Model"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Init Method"""
        super().__init__(*args, **kwargs)
