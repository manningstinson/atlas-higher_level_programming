
import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_constructor(self):
        obj1 = Base()
        obj2 = Base()
        self.assertIsInstance(obj1, Base)
        self.assertIsInstance(obj2, Base)
        self.assertNotEqual(obj1.id, obj2.id)

    def test_to_json_string(self):
        obj = Base()
        json_string = Base.to_json_string([obj.to_dictionary()])
        self.assertEqual(json_string, '[{"id": 1}]')

    def test_save_to_file(self):
        obj = Base()
        Base.save_to_file([obj])
        with open("Base.json", "r") as file:
            content = file.read()
            self.assertEqual(content, '[{"id": 1}]')

    def test_from_json_string(self):
        json_string = '[{"id": 1}]'
        obj_list = Base.from_json_string(json_string)
        self.assertEqual(obj_list, [{'id': 1}])

    def test_create(self):
        obj = Base.create(**{'id': 1, 'width': 2, 'height': 3})
        self.assertIsInstance(obj, Base)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 3)

    def test_update(self):
        obj = Base()
        obj.update(id=2, width=5, height=7)
        self.assertEqual(obj.id, 2)
        self.assertEqual(obj.width, 5)
        self.assertEqual(obj.height, 7)

    def test_to_dictionary(self):
        obj = Base(**{'id': 1, 'width': 2, 'height': 3})
        dictionary = obj.to_dictionary()
        self.assertEqual(dictionary, {'id': 1, 'width': 2, 'height': 3})

if __name__ == '__main__':
    unittest.main()
