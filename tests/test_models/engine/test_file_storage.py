import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class FileStorageTestCase(unittest.TestCase):
    def setUp(self):
        # Create a new instance of FileStorage before each test
        self.storage = FileStorage()


def teardown(self):
    # Clean up any created objects after each test
    self.storage = None

def test_all(self):
    #Test the all() method
    objects = self.storage.all()
    self.assertEqual(objects, {}) #The initial dictionary should be empty

    # Create a BaseModel instance and add it to the storage
    base_model = BaseModel()
    self.storage.new(base_model)
    objects = self.storage.all()
    self.assertEqual(len(objects), 1) # There should be one object in the dictionary
    self.assertIn(f"BaseModel. {base_model.id}", objects)  # The object should be present with the correct key

def test_new(self):
    # Test in new() method
    objects = self.storage.all()
    self.assertEqual(objects, {}) # The initial dictionary should be empty

    # Create a BaseModel instance and add it to the storage
    base_model = BaseModel()
    self.storage.new(base_model)
    objects = self.storage.all()
    self.assertEqual(len(objects), 1) # There should be one object in the dictionary
    self.assertIn(f"BaseModel.{base_model.id}", objects) # The object should be present with the correct key

def test_save_reload(self):
    objects = self.storage.all()
    self.assertEqual(objects, {} )  # The initial dictionary should be empty

    # Create a BaseModel instance and add it to the storage
    base_model = BaseModel()
    self.storage.new(base_model)

    # Save the objects to the file and reload them
    self.storage.save()
    self.storage.reload()
    objects = self.storage.all()
    self.assertEqual(len(objects, 1)) # There should be one object in the dictionary after reloading
    self.assertIn(f"BaseModel.{base_model.id}", objects) # The object should be present with the correct key

def test_from_dict(self):
    # Test from_dict(method)
    obj_dict = {
        "__class__": "BaseModel",
        "id": "12345",
        "created_at":"2023-06-10T12:00:00.000000",
        "updated_at": "2023-06-10T12:30:00.000000",
        "name": "Test Model"
    }

    base_model = self.storage.from_dict(obj_dict)
    self.assertIsInstance(base_model, BaseModel)  # The object should be an instance of BaseModel
    self.assertEqual(base_model.id, "12345")  # The id should match the value in the dictionary
    self.assertEqual(base_model.name, "Test Model")  # The name should match the value in the dictionary

    # The datetime attributes should be converted to datetime objects
    self.assertEqual(base_model.created_at.year, 2023)
    self.assertEqual(base_model.created_at.month, 6)
    self.assertEqual(base_model.created_at.day, 10)
    self.assertEqual(base_model.created_at.hour, 12)
    self.assertEqual(base_model.created_at.minute, 0)
    self.assertEqual(base_model.created_at.second, 0)
    self.assertEqual(base_model.created_at.microsecond, 0)

if __name__ == '__main__':
    unittest.main()