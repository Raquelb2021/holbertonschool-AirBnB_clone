#!/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """calls the save method and checks that
    the updated_at attribute was updated
    """
    def test_save(self):
        # Create an instance of BaseModel.
        my_model = BaseModel()
        # Store the current updated_at attribute in old_updated_at.
        old_updated_at = my_model.updated_at
        # Call the save() method on the BaseModel instance.
        my_model.save()
        # Check if the updated_at attribute has been updated by the save() method.
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_to_dict(self):
        """calls the to_dict method
        and checks that the returned dictionary contains the expected
        keys and values
        """
        my_model = BaseModel()
        # Call the to_dict() method on the BaseModel instance and store the result in my_dict.
        my_dict = my_model.to_dict()
        # Check if the __class__ key in my_dict has the correct value 'BaseModel'.
        self.assertEqual(my_dict['__class__'], 'BaseModel')
        # Check if the id key in my_dict has the same value as the id attribute of the BaseModel instance.
        self.assertEqual(my_dict['id'], my_model.id)
        # Check if the created_at key in my_dict has the same value as the created_at attribute of the BaseModel instance.
        self.assertEqual(my_dict[
            'created_at'], my_model.created_at.isoformat())
        self.assertEqual(my_dict[
            'updated_at'], my_model.updated_at.isoformat())

    def test_id(self):
        """
        checks if the id attribute us a string
        """
        my_model = BaseModel()  # Create an instance of BaseModel.
        self.assertIsInstance(my_model.id, str)  # Check if the id attribute of the BaseModel instance is of type string.

    def test_created_at(self):
        """
        checks if the created_at attribute is a datetime
        object
        """
        my_model = BaseModel()  # Create an instance of BaseModel.
        self.assertIsInstance(my_model.created_at, datetime)  # Check if the created_at attribute of the BaseModel instance is of type datetime.

    def test_str(self):
        """
        calls __str__ method, and checks
        that the returned string is in the expected format
        """
        my_model = BaseModel()  # Create an instance of BaseModel.
        expected_str = '[BaseModel] ({}) {}'.format(
            my_model.id,
            my_model.__dict__
            )  # Define the expected string output of the __str__() method on the BaseModel instance.
        self.assertEqual(str(my_model), expected_str)  # Check if calling str() on the BaseModel instance produces the expected string.


if __name__ == '__main__':
    unittest.main()
