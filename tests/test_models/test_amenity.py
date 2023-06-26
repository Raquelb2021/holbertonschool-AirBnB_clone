#!/usr/bin/python3
import unittest
from models.amenity import Amenity
"""Unittest testing a empty string"""


class TestAmenity(unittest.TestCase):  # This class is defined to contain test cases for the Amenity class. It inherits from unittest.TestCase.
    def test_name(self):  # This method tests the name attribute of the Amenity class.
        amenity = Amenity()  # Create an instance of Amenity.
        self.assertEqual(amenity.name, '')  # Check if the name attribute of the Amenity instance has the expected value of an empty string.


if __name__ == '__main__':
    unittest.main()
