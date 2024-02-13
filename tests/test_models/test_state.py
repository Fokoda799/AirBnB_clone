#!/usr/bin/python3
import unittest
from models.state import State
from datetime import datetime


class TestStateModel(unittest.TestCase):
    """Test cases for the State model"""

    def test_state_creation(self):
        """Test the creation of a State instance"""
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsNotNone(state.id)
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)

    def test_state_attributes(self):
        """Test the attributes of the State class"""
        state = State()
        self.assertEqual(state.name, "")

    def test_state_str_representation(self):
        """Test the __str__ method of the State class"""
        state = State()
        str_representation = str(state)
        self.assertIn("[State]", str_representation)
        self.assertIn(str(state.id), str_representation)
        self.assertIn("created_at", str_representation)
        self.assertIn("updated_at", str_representation)

    def test_state_save_method(self):
        """Test the save method of the State class"""
        state = State()
        initial_updated_at = state.updated_at
        state.save()
        self.assertNotEqual(state.updated_at, initial_updated_at)

    def test_state_to_dict_method(self):
        """Test the to_dict method of the State class"""
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertIn('id', state_dict)
        self.assertIn('created_at', state_dict)
        self.assertIn('updated_at', state_dict)
        self.assertIn('__class__', state_dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(state_dict['name'], "")


if __name__ == '__main__':
    unittest.main()
