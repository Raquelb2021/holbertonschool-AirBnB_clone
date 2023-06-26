#!/usr/bin/python3

import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_name(self):  # Test case for checking the initial name attribute of State
        state = State()
        self.assertEqual(state.name, '')
        state.name = 'California'  # Modifying the name attribute
        self.assertEqual(state.name, 'California')  # Test case for checking if the name attribute is modified correctly


if __name__ == '__main__':
    unittest.main()
