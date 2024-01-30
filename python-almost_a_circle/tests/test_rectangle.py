import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_rectangle_creation_exists(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertIsInstance(rect, Rectangle)

    def test_str_representation_exists(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(str(rect), "[Rectangle] (1) 3/4 - 1/2")

    def test_display_exists(self):
        rect = Rectangle(1, 2, 3, 4)
        with self.assertRaises(AttributeError):
            rect.display()

    def test_area_exists(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect.area(), 2)

    def test_update_exists(self):
        rect = Rectangle(1, 2, 3, 4)
        rect.update(5, 6, 7, 8, 9)
        self.assertEqual(str(rect), "[Rectangle] (5) 7/8 - 6/7")

    def test_to_dictionary_exists(self):
        rect = Rectangle(1, 2, 3, 4)
        rect_dict = rect.to_dictionary()
        self.assertEqual(rect_dict, {'id': 1, 'width': 1, 'height': 2, 'x': 3, 'y': 4})

    def test_load_from_file_exists(self):
        with self.assertRaises(FileNotFoundError):
            Rectangle.load_from_file()

if __name__ == '__main__':
    unittest.main()
