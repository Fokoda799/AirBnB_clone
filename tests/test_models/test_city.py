#!/usr/bin/python3
import unittest
from models.city import City
from datetime import datetime


class TestCityModel(unittest.TestCase):
    """Test cases for the City model"""

    def test_city_creation(self):
        """Test the creation of a City instance"""
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsNotNone(city.id)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)

    def test_city_attributes(self):
        """Test the attributes of the City class"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_str_representation(self):
        """Test the __str__ method of the City class"""
        city = City()
        str_representation = str(city)
        self.assertIn("[City]", str_representation)
        self.assertIn(str(city.id), str_representation)
        self.assertIn("created_at", str_representation)
        self.assertIn("updated_at", str_representation)

    def test_city_save_method(self):
        """Test the save method of the City class"""
        city = City()
        initial_updated_at = city.updated_at
        city.save()
        self.assertNotEqual(city.updated_at, initial_updated_at)

    def test_city_to_dict_method(self):
        """Test the to_dict method of the City class"""
        city = City()
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertIn('id', city_dict)
        self.assertIn('created_at', city_dict)
        self.assertIn('updated_at', city_dict)
        self.assertIn('__class__', city_dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['state_id'], "")
        self.assertEqual(city_dict['name'], "")


if __name__ == '__main__':
    unittest.main()
