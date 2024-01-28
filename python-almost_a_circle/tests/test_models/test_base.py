#!/usr/bin/python3
"""Unit tests for models.base"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_constructor_with_id(self):
        obj = Base(5)
        self.assertEqual(obj.id, 5)

    def test_constructor_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, obj2.id - 1)

    def test_to_json_string_empty_list(self):
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_to_json_string_non_empty_list(self):
        json_str = Base.to_json_string([{'key': 'value'}])
        self.assertEqual(json_str, '[{"key": "value"}]')


if __name__ == '__main__':
    unittest.main()
