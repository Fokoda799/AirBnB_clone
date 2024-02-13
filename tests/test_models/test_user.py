#!/usr/bin/python3
"""User Model"""
import unittest
from models.user import User
from datetime import datetime


class TestUserModel(unittest.TestCase):
    """Test cases for the User model"""

    def test_user_creation(self):
        """Test the creation of a User instance"""
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsNotNone(user.id)
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)

    def test_user_attributes(self):
        """Test the attributes of the User class"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_str_representation(self):
        """Test the __str__ method of the User class"""
        user = User()
        str_representation = str(user)
        self.assertIn("[User]", str_representation)
        self.assertIn(str(user.id), str_representation)
        self.assertIn("created_at", str_representation)
        self.assertIn("updated_at", str_representation)

    def test_user_save_method(self):
        """Test the save method of the User class"""
        user = User()
        initial_updated_at = user.updated_at
        user.save()
        self.assertNotEqual(user.updated_at, initial_updated_at)

    def test_user_to_dict_method(self):
        """Test the to_dict method of the User class"""
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIn('id', user_dict)
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)
        self.assertIn('__class__', user_dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['email'], "")
        self.assertEqual(user_dict['password'], "")
        self.assertEqual(user_dict['first_name'], "")
        self.assertEqual(user_dict['last_name'], "")


if __name__ == '__main__':
    unittest.main()
