#!/usr/bin/python3

import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    def test_city_id(self):  # Test case for checking the initial city_id attribute of Place
        place = Place()
        self.assertEqual(place.city_id, '')

    def test_user_id(self):  # Test case for checking the initial user_id attribute of Place
        place = Place()
        self.assertEqual(place.user_id, '')

    def test_name(self):  # Test case for checking the initial name attribute of Place
        place = Place()
        self.assertEqual(place.name, '')

    def test_description(self):  # Test case for checking the initial description attribute of Place
        place = Place()
        self.assertEqual(place.description, '')

    def test_number_rooms(self):  # Test case for checking the initial number_rooms attribute of Place
        place = Place()
        self.assertEqual(place.number_rooms, 0)

    def test_number_bathrooms(self):  # Test case for checking the initial number_bathrooms attribute of Place
        place = Place()
        self.assertEqual(place.number_bathrooms, 0)

    def test_max_guest(self):  # Test case for checking the initial max_guest attribute of Place
        place = Place()
        self.assertEqual(place.max_guest, 0)

    def test_price_by_night(self):  # Test case for checking the initial price_by_night attribute of Place
        place = Place()
        self.assertEqual(place.price_by_night, 0)

    def test_latitude(self):  # Test case for checking the initial latitude attribute of Place
        place = Place()
        self.assertEqual(place.latitude, 0.0)

    def test_longitude(self):  # Test case for checking the initial longitude attribute of Place
        place = Place()
        self.assertEqual(place.longitude, 0.0)

    def test_amenity_ids(self):  # Test case for checking the initial amenity_ids attribute of Place
        place = Place()
        self.assertEqual(place.amenity_ids, [])


if __name__ == '__main__':
    unittest.main()
