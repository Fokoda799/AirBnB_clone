#!/usr/bin/python3
"""Place Model"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Palce class"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_romms = 0
    number_bathromms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
