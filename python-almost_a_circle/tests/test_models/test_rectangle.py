# tests/test_models/test_rectangle.py
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_constructor(self):
        rect = Rectangle(1, 2)
        self.assertIsInstance(rect, Rectangle)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)

    # Add more test cases for the Rectangle class if needed
