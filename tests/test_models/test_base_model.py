import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_base_model(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        self.assertEqual(my_model.name, "My First Model")
        self.assertEqual(my_model.my_number, 89)

        # Testing __str__ method
        expected_str = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), expected_str)


        # Testing save method
        prev_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(my_model.updated_at, prev_updated_at)

        # Testing to_dict method
        my_model_json = my_model.to_dict()
        expected_dict = my_model.__dict__.copy()
        expected_dict['__class__'] = 'BaseModel'
        expected_dict['created_at'] = expected_dict['created_at'].isoformat()
        expected_dict['updated_at'] = expected_dict['updated_at'].isoformat()
        self.assertEqual(my_model_json, expected_dict)


if __name__ == '__main__':
    unittest.main()
