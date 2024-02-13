#!/usr/bin/python3
"""Unit testing of BaseModel class"""
import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class BaseModel_test(unittest.TestCase):
    """Test cases of BaseModel class"""

    def setUp(self):
        pass

    def test_init_default_value(self):
        """Testing initialization with default values"""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertEqual(type(obj.id), str)
        self.assertEqual(type(obj.created_at), datetime)
        self.assertEqual(type(obj.updated_at), datetime)

    def test_init_with_args(self):
        """Testing initialization with specified values"""
        id = 'test_id'
        ca = datetime.utcnow().isoformat()
        ua = datetime.utcnow().isoformat()
        obj = BaseModel(id=id, created_at=ca, updated_at=ua)
        self.assertEqual(obj.id, id)
        self.assertEqual(obj.created_at, datetime.fromisoformat(ca))
        self.assertEqual(obj.updated_at, datetime.fromisoformat(ua))

    def test_save(self):
        """Testing the save method"""
        obj = BaseModel()
        initial_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, initial_updated_at)

    def test_to_dict(self):
        """Testing the to_dict method"""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('__class__', obj_dict)

    def test_str(self):
        """Testing the __str__ method"""
        obj = BaseModel()
        obj_str = str(obj)
        self.assertIsInstance(obj_str, str)
        self.assertIn(obj.id, obj_str)
        self.assertIn(str(obj.__class__.__name__), obj_str)


if __name__ == '__main__':
    unittest.main()
