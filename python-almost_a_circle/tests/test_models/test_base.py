
import unittest
from base import Rectangle, Base

class TestBaseMethods(unittest.TestCase):

    def test_base_auto_id(self):
        r1 = Base()
        self.assertEqual(r1.id, 1)

    def test_base_auto_id_increment(self):
        r1 = Base()
        r2 = Base()
        self.assertEqual(r2.id, r1.id + 1)

    def test_base_custom_id(self):
        r1 = Base(89)
        self.assertEqual(r1.id, 89)

    def test_to_json_string_none(self):
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_to_json_string_empty_list(self):
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    # Add more test methods for the remaining cases...

if __name__ == '__main__':
    unittest.main()
