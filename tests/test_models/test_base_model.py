#!/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_save(self):
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_to_dict(self):
        my_model = BaseModel()
        my_dict = my_model.to_dict()
        self.assertEqual(my_dict['__class__'], 'BaseModel')
        self.assertEqual(my_dict['id'], my_model.id)
        self.assertEqual(my_dict['created_at'], my_model.created_at.isoformat())
        self.assertEqual(my_dict['updated_at'], my_model.updated_at.isoformat())

    def test_id(self):
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)

    def test_created_at(self):
        my_model = BaseModel()
        self.assertIsInstance(my_model.created_at, datetime)

    def test_str(self):
        my_model = BaseModel()
        expected_str = '[BaseModel] ({}) {}'.format(
            my_model.id,
            my_model.__dict__
            )
        self.assertEqual(str(my_model), expected_str)

if __name__ == '__main__':
    unittest.main()

