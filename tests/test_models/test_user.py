#!/usr/bin/python3
import unittest
from models.user import User
"""unittest testing an empty string"""


class TestUser(unittest.TestCase):
    def test_email(self):  # Test case for checking the initial email attribute of User
        user = User()
        self.assertEqual(user.email, '')

    def test_password(self):
        user = User()  # Test case for checking the initial password attribute of User
        self.assertEqual(user.password, '')

    def test_first_name(self):
        user = User()  # Test case for checking the initial first_name attribute of User
        self.assertEqual(user.first_name, '')

    def test_last_name(self):
        user = User()  # Test case for checking the initial last_name attribute of User
        self.assertEqual(user.last_name, '')


if __name__ == '__main__':
    unittest.main()
