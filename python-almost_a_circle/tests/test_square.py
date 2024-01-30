import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_constructor(self):
        square = Square(5, 2, 3, 4)
        self.assertIsInstance(square, Square)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 4)

    def test_str_method(self):
        square = Square(5, 2, 3, 4)
        self.assertEqual(str(square), "[Square] (4) 2/3 - 5")

    def test_update_method(self):
        square = Square(5, 2, 3, 4)
        square.update(6, 7, 8, 9)
        self.assertEqual(square.id, 6)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 8)
        self.assertEqual(square.y, 9)

    def test_to_dictionary_method(self):
        square = Square(5, 2, 3, 4)
        square_dict = square.to_dictionary()
        expected_dict = {'id': 4, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(square_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()
