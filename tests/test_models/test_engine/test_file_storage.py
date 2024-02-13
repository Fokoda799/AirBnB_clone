#!/usr/bin/python3
"""Test cases for File Storage Model"""
import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """Testing FileStorage class"""
    def setUp(self):
        """Set up objects needed"""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up"""
        try:
            os.remove('file.json')
        except Exception as e:
            pass
        self.storage.reload()

    def test_file_storage_serialization(self):
        """Testing file storage seriallization"""
        obj = User()
        obj.name = "Test User"
        obj.email = "test@user.com"
        obj.save()
        obj_name = f'User.{obj.id}'
        self.assertIn(obj_name, self.storage.all())
        loaded_obj = self.storage.all()[obj_name]
        self.assertEqual(obj.to_dict(), loaded_obj.to_dict())

    def test_file_storage_deserialization(self):
        """Testing file storage deseriallization"""
        obj = User()
        obj.name = "Test User"
        obj.email = "test@user.com"
        obj.save()
        obj_name = f'User.{obj.id}'
        loaded_storage = FileStorage()
        loaded_storage.reload()
        self.assertIn(obj_name, loaded_storage.all())

    def test_file_storage_serialization_multiple_objects(self):
        """Testing File storage serialization multiple obj"""
        city = City()
        city.name = "Fas"
        city.save()
        city_name = f'City.{city.id}'
        place = Place()
        place.name = "lili"
        place.save()
        place_name = f'Place.{place.id}'
        self.assertIn(city_name, self.storage.all())
        self.assertIn(place_name, self.storage.all())

    def test_file_storage_deserialization_multiple_objects(self):
        """Testing File storage deserialization multiple obj"""
        review = Review()
        review.text = "Its so good"
        review.save()
        review_name = f'Review.{review.id}'
        amenity = Amenity()
        amenity.name = "Loot"
        amenity.save()
        amenity_name = f'Amenity.{amenity.id}'
        loaded_storage = FileStorage()
        loaded_storage.reload()
        self.assertIn(review_name, loaded_storage.all())
        self.assertIn(amenity_name, loaded_storage.all())


if __name__ == '__main__':
    unittest.main()
