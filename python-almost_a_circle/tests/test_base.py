import unittest
from your_module_name import Base, Rectangle

class TestBaseClass(unittest.TestCase):

    def test_auto_assign_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_auto_assign_incremental_id(self):
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        self.assertEqual(obj3.id, obj2.id + 1)

    def test_specified_id(self):
        obj = Base(89)
        self.assertEqual(obj.id, 89)

    def test_to_json_string_none(self):
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_to_json_string_empty_list(self):
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_with_data(self):
        data = [{'id': 12}]
        result = Base.to_json_string(data)
        self.assertEqual(result, '[{"id": 12}]')

    def test_from_json_string_none(self):
        result = Base.from_json_string(None)
        self.assertEqual(result, [])

    def test_from_json_string_empty_string(self):
        result = Base.from_json_string("[]")
        self.assertEqual(result, [])

    def test_from_json_string_with_data(self):
        json_str = '[{"id": 89}]'
        result = Base.from_json_string(json_str)
        self.assertEqual(result, [{'id': 89}])

if __name__ == '__main__':
    unittest.main()
