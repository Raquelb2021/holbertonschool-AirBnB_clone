#!/usr/bin/python3
import unittest
from models.user import User
"""unittest testing an empty string"""


class TestUser(unittest.TestCase):
    def test_email(self):
        user = User()
        self.assertEqual(user.email, '')

    def test_password(self):
        user = User()
        self.assertEqual(user.password, '')

    def test_first_name(self):
        user = User()
        self.assertEqual(user.first_name, '')

    def test_last_name(self):
        user = User()
        self.assertEqual(user.last_name, '')


if __name__ == '__main__':
    unittest.main()
