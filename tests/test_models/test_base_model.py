#!/usr/bin/python3
"""
unittest for models/base_model.py
"""
import models
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base = BaseModel()

    def tearDown(self):
        del self.base

    def test_id(self):
        self.assertIsInstance(self.base.id, str)

    def test_created_at(self):
        self.assertIsInstance(self.base.created_at, datetime)

    def test_updated_at(self):
        self.assertIsInstance(self.base.updated_at, datetime)

    def test_str(self):
        expected_str = "[BaseModel] ({}) {}".format(
            self.base.id, self.base.__dict__)
        self.assertEqual(str(self.base), expected_str)

    def test_save(self):
        old_updated_at = self.base.updated_at

    def test_to_dict(self):
        base_dict = self.base.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertEqual(base_dict["id"], self.base.id)
        self.assertEqual(
                base_dict["created_at"],
                self.base.created_at.isoformat())
        self.assertEqual(
                base_dict["updated_at"],
                self.base.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
