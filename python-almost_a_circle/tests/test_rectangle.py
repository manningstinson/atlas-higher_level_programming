import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_exists(self):
        r = Rectangle(1, 2)
        self.assertIsInstance(r, Rectangle)

    def test_exists_with_three_arguments(self):
        r = Rectangle(1, 2, 3)
        self.assertIsInstance(r, Rectangle)

    def test_exists_with_four_arguments(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertIsInstance(r, Rectangle)

    def test_invalid_width_string(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_invalid_height_string(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_invalid_x_string(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_invalid_y_string(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_exists_with_five_arguments(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertIsInstance(r, Rectangle)

    def test_invalid_negative_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_invalid_negative_height(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_valid_zero_width(self):
        r = Rectangle(0, 2)
        self.assertIsInstance(r, Rectangle)

    def test_valid_zero_height(self):
        r = Rectangle(1, 0)
        self.assertIsInstance(r, Rectangle)

    def test_invalid_negative_x(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_invalid_negative_y(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

if __name__ == '__main__':
    unittest.main()
