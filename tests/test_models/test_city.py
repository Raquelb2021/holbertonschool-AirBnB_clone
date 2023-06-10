#!/usr/bin/python3
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def test_state_id(self):
        city = City()
        self.assertEqual(city.state_id, '')

    def test_name(self):
        city = City()
        self.assertEqual(city.name, '')


if __name__ == '__main__':
    unittest.main()
