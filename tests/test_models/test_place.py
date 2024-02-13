#!/usr/bin/python3
import unittest
from models.place import Place
from datetime import datetime


class TestPlaceModel(unittest.TestCase):
    """Test cases for the Place model"""

    def test_place_creation(self):
        """Test the creation of a Place instance"""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsNotNone(place.id)
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)

    def test_place_attributes(self):
        """Test the attributes of the Place class"""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_place_str_representation(self):
        """Test the __str__ method of the Place class"""
        place = Place()
        str_representation = str(place)
        self.assertIn("[Place]", str_representation)
        self.assertIn(str(place.id), str_representation)
        self.assertIn("created_at", str_representation)
        self.assertIn("updated_at", str_representation)

    def test_place_save_method(self):
        """Test the save method of the Place class"""
        place = Place()
        initial_updated_at = place.updated_at
        place.save()
        self.assertNotEqual(place.updated_at, initial_updated_at)

    def test_place_to_dict_method(self):
        """Test the to_dict method of the Place class"""
        place = Place()
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertIn('id', place_dict)
        self.assertIn('created_at', place_dict)
        self.assertIn('updated_at', place_dict)
        self.assertIn('__class__', place_dict)
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(place_dict['city_id'], "")
        self.assertEqual(place_dict['user_id'], "")
        self.assertEqual(place_dict['name'], "")
        self.assertEqual(place_dict['description'], "")
        self.assertEqual(place_dict['number_rooms'], 0)
        self.assertEqual(place_dict['number_bathrooms'], 0)
        self.assertEqual(place_dict['max_guest'], 0)
        self.assertEqual(place_dict['price_by_night'], 0)
        self.assertEqual(place_dict['latitude'], 0.0)
        self.assertEqual(place_dict['longitude'], 0.0)
        self.assertEqual(place_dict['amenity_ids'], [])


if __name__ == '__main__':
    unittest.main()
