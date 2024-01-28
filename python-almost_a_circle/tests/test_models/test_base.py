#!/usr/bin/python3
"""Unit tests for models.base"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_auto_assign_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id + 1, obj2.id)

    def test_save_passed_id(self):
        obj = Base(89)
        self.assertEqual(obj.id, 89)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{ "id": 89 }]'), [{'id': 89}])


if __name__ == '__main__':
    unittest.main()
