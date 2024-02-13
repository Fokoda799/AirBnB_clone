#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenityModel(unittest.TestCase):
    """Test cases for the Amenity model"""

    def test_amenity_creation(self):
        """Test the creation of an Amenity instance"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsNotNone(amenity.id)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)

    def test_amenity_attributes(self):
        """Test the attributes of the Amenity class"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_str_representation(self):
        """Test the __str__ method of the Amenity class"""
        amenity = Amenity()
        str_representation = str(amenity)
        self.assertIn("[Amenity]", str_representation)
        self.assertIn(str(amenity.id), str_representation)
        self.assertIn("created_at", str_representation)
        self.assertIn("updated_at", str_representation)

    def test_amenity_save_method(self):
        """Test the save method of the Amenity class"""
        amenity = Amenity()
        initial_updated_at = amenity.updated_at
        amenity.save()
        self.assertNotEqual(amenity.updated_at, initial_updated_at)

    def test_amenity_to_dict_method(self):
        """Test the to_dict method of the Amenity class"""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertIn('id', amenity_dict)
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)
        self.assertIn('__class__', amenity_dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['name'], "")


if __name__ == '__main__':
    unittest.main()
