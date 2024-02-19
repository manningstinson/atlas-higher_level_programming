import io
import sys
import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_auto_assign_id_exists(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_auto_assign_id_incremented_exists(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_base_with_id_exists(self):
        obj = Base(89)
        self.assertEqual(obj.id, 89)

    def test_to_json_string_exists(self):
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_to_json_string_empty_list_exists(self):
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_to_json_string_with_id_exists(self):
        json_str = Base.to_json_string([{'id': 12}])
        self.assertEqual(json_str, '[{"id": 12}]')

    def test_to_json_string_returns_string_exists(self):
        json_str = Base.to_json_string([{'id': 12}])
        self.assertIsInstance(json_str, str)

    def test_from_json_string_exists(self):
        obj_list = Base.from_json_string(None)
        self.assertEqual(obj_list, [])

    def test_from_json_string_empty_list_exists(self):
        obj_list = Base.from_json_string("[]")
        self.assertEqual(obj_list, [])

    def test_from_json_string_with_id_exists(self):
        obj_list = Base.from_json_string('[{ "id": 89 }]')
        self.assertEqual(obj_list, [{'id': 89}])

    def test_from_json_string_returns_list_exists(self):
        obj_list = Base.from_json_string('[{ "id": 89 }]')
        self.assertIsInstance(obj_list, list)

if __name__ == '__main__':
    unittest.main()
