import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class FileStorageTestCase(unittest.TestCase):
    def setUp(self):
    # Create an instance of FileStorage
        self.storage = FileStorage()

def teardown(self):
    # Remove the file.json created during testing
    if os.path.exists("file.json"):
        os.remove("file.json")

def test_all(self):
    # Test if all() returns the correct dictionary of objects
            self.assertEqual(self.storage.all(), {})
            #file storage
            obj1 = BaseModel()
            self.storage.new(obj1)
            self.storage.save()
            
            # Clear the objects dictionary
            self.storage.__objects = {}
            
            # Call reload() to load the objects from the JSON file
            self.storage.reload()
            
            # Check if the objects are correctly loaded
            self.assertEqual(len(self.storage.all()), 7)
            self.assertIn(f"{type(obj1).__name__}.{obj1.id}", self.storage.all())

if __name__ == "__main__":
    unittest.main()