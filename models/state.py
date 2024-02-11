#!/usr/bin/python3
"""State Model"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Init Method"""
        super().__init__(*args, **kwargs)
