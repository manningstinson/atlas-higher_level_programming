import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_constructor(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_string_representation(self):
        r = Rectangle(3, 4, 1, 2, 7)
        self.assertEqual(str(r), "[Rectangle] (7) 1/2 - 3/4")

    def test_display_method(self):
        r = Rectangle(2, 2)
        with self.assertLogs() as logs:
            r.display()
        self.assertEqual(logs.output, [''])

    def test_update_method(self):
        r = Rectangle(2, 2)
        r.update(3, 4, 5, 6, 7)
        self.assertEqual(str(r), "[Rectangle] (3) 6/7 - 4/5")

    def test_to_dictionary_method(self):
        r = Rectangle(2, 2, 3, 4, 5)
        self.assertEqual(r.to_dictionary(), {'id': 5, 'width': 2, 'height': 2, 'x': 3, 'y': 4})

if __name__ == '__main__':
    unittest.main()
