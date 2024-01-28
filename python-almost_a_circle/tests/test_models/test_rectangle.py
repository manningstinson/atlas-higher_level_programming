#!/usr/bin/python3
"""Unit tests for models.rectangle"""

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_constructor(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2)
        with self.assertRaises(ValueError):
            r = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 3, -4)

    def test_area(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.area(), 2)

    def test_to_dictionary(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.to_dictionary(), {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4})


if __name__ == '__main__':
    unittest.main()
