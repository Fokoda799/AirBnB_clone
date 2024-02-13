#!/usr/bin/python3
import unittest
from models.review import Review
from datetime import datetime


class TestReviewModel(unittest.TestCase):
    """Test cases for the Review model"""

    def test_review_creation(self):
        """Test the creation of a Review instance"""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsNotNone(review.id)
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)

    def test_review_attributes(self):
        """Test the attributes of the Review class"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_str_representation(self):
        """Test the __str__ method of the Review class"""
        review = Review()
        str_representation = str(review)
        self.assertIn("[Review]", str_representation)
        self.assertIn(str(review.id), str_representation)
        self.assertIn("created_at", str_representation)
        self.assertIn("updated_at", str_representation)

    def test_review_save_method(self):
        """Test the save method of the Review class"""
        review = Review()
        initial_updated_at = review.updated_at
        review.save()
        self.assertNotEqual(review.updated_at, initial_updated_at)

    def test_review_to_dict_method(self):
        """Test the to_dict method of the Review class"""
        review = Review()
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertIn('id', review_dict)
        self.assertIn('created_at', review_dict)
        self.assertIn('updated_at', review_dict)
        self.assertIn('__class__', review_dict)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(review_dict['place_id'], "")
        self.assertEqual(review_dict['user_id'], "")
        self.assertEqual(review_dict['text'], "")


if __name__ == '__main__':
    unittest.main()
