import io
import sys
import unittest
from models.base import Base
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_square_creation_exists(self):
        square = Square(1, 2, 3)
        self.assertIsInstance(square, Square)

    def test_str_representation_exists(self):
        square = Square(1, 2, 3)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 1")

    def test_display_exists(self):
        square = Square(1, 2, 3)
        with self.assertRaises(AttributeError):
            square.display()

    def test_area_exists(self):
        square = Square(1, 2, 3)
        self.assertEqual(square.area(), 1)

    def test_update_exists(self):
        square = Square(1, 2, 3)
        square.update(5, 6, 7, 8)
        self.assertEqual(str(square), "[Square] (5) 7/8 - 6")

    def test_to_dictionary_exists(self):
        square = Square(1, 2, 3)
        square_dict = square.to_dictionary()
        self.assertEqual(square_dict, {'id': 1, 'size': 1, 'x': 2, 'y': 3})

    def test_load_from_file_exists(self):
        with self.assertRaises(FileNotFoundError):
            Square.load_from_file()

if __name__ == '__main__':
    unittest.main()
