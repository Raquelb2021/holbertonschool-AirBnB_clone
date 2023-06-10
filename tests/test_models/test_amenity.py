#!/usr/bin/python3
import unittest
from models.amenity import Amenity
"""Unittest testing a empty string"""


class TestAmenity(unittest.TestCase):
    def test_name(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, '')


if __name__ == '__main__':
    unittest.main()
