
# tests/test_models/test_square.py
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_constructor(self):
        square = Square(3)
        self.assertIsInstance(square, Square)
        self.assertEqual(square.size, 3)

    # Add more test cases for the Square class if needed
