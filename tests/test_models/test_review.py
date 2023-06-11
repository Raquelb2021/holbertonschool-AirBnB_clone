#!/usr/bin/python3
import unittest
from models.review import Review
"""unittest testing an empty string"""

class TestReview(unittest.TestCase):
    def test_place_id(self):
        review = Review()
        self.assertEqual(review.place_id, '')

    def test_user_id(self):
        review = Review()
        self.assertEqual(review.user_id, '')

    def test_text(self):
        review = Review()
        self.assertEqual(review.text, '')


if __name__ == '__main__':
    unittest.main()
