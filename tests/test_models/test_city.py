#!/usr/bin/python3
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def test_state_id(self):
        city = City()  # Test case for checking the initial state_id attribute of City
        self.assertEqual(city.state_id, '')

    def test_name(self):
        city = City()  # Test case for checking the initial name attribute of City
        self.assertEqual(city.name, '')


if __name__ == '__main__':
    unittest.main()
