#!/usr/bin/python3

import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    def test_city_id(self):
        place = Place()
        self.assertEqual(place.city_id, '')

    def test_user_id(self):
        place = Place()
        self.assertEqual(place.user_id, '')

    def test_name(self):
        place = Place()
        self.assertEqual(place.name, '')

    def test_description(self):
        place = Place()
        self.assertEqual(place.description, '')

    def test_number_rooms(self):
        place = Place()
        self.assertEqual(place.number_rooms, 0)

    def test_number_bathrooms(self):
        place = Place()
        self.assertEqual(place.number_bathrooms, 0)

    def test_max_guest(self):
        place = Place()
        self.assertEqual(place.max_guest, 0)

    def test_price_by_night(self):
        place = Place()
        self.assertEqual(place.price_by_night, 0)

    def test_latitude(self):
        place = Place()
        self.assertEqual(place.latitude, 0.0)

    def test_longitude(self):
        place = Place()
        self.assertEqual(place.longitude, 0.0)

    def test_amenity_ids(self):
        place = Place()
        self.assertEqual(place.amenity_ids, [])


if __name__ == '__main__':
    unittest.main()
