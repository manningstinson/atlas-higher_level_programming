#!/usr/bin/python3
"""Unit tests for models.square"""

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_constructor(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 4)

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            s = Square(-1)
        with self.assertRaises(ValueError):
            s = Square(1, -2)
        with self.assertRaises(ValueError):
            s = Square(1, 2, -3)

    def test_area(self):
        s = Square(2)
        self.assertEqual(s.area(), 4)

    def test_to_dictionary(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.to_dictionary(), {'id': 4, 'size': 1, 'x': 2, 'y': 3})


if __name__ == '__main__':
    unittest.main()
