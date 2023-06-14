#!/usr/bin/python3
"""Tests for the file storage"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.fs = FileStorage()
        self.fs._FileStorage__objects.clear()

    def test_all(self):
        self.assertEqual(self.fs.all(), {})

    def test_new(self):
        bm = BaseModel()
        self.fs.new(bm)
        key = "BaseModel.{}".format(bm.id)
        self.assertIn(key, self.fs.all())
        self.assertEqual(self.fs.all()[key], bm)

    def test_save(self):
        bm = BaseModel()
        self.fs.new(bm)
        self.fs.save()
        with open(self.fs._FileStorage__file_path, 'r') as f:
            content = f.read()
            key = "BaseModel.{}".format(bm.id)
            self.assertIn(key, content)

    def test_reload(self):
        bm = BaseModel()
        self.fs.new(bm)
        self.fs.save()
        key = "BaseModel.{}".format(bm.id)
        del self.fs._FileStorage__objects[key]
        self.assertNotIn(key, self.fs.all())
        self.fs.reload()
        self.assertIn(key, self.fs.all())

if __name__ == '__main__':
    unittest.main()
