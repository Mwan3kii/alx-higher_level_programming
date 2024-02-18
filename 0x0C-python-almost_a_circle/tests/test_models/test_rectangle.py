import unittest
from models.rectangle import Rectangle
from unittest.mock import patch
import sys
import io
import os

class TestRectangle(unittest.TestCase):
    def test_init(self):
        r = Rectangle(10, 20, 5, 8, 1)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 8)

    def test_width_setter(self):
        r = Rectangle(10, 20)
        r.width = 15
        self.assertEqual(r.width, 15)

        with self.assertRaises(ValueError):
            r.width = -7

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            Rectangle(2, -4)

    def test_x_setter(self):
        r = Rectangle(10, 20)
        r.x = 4
        self.assertEqual(r.x, 4)

        with self.assertRaises(ValueError):
            r.x = -2

    def test_y_setter(self):
        r = Rectangle(10, 20)
        r.y = 9
        self.assertEqual(r.y, 9)

        with self.assertRaises(ValueError):
            r.y = -3

    def test_area(self):
        r = Rectangle(6, 10)
        self.assertEqual(r.area(), 60)

    def test_display(self):
        r = Rectangle(4, 3)
        expected = "####\n####\n####"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue().strip(), expected)

    def test_str(self):
        r = Rectangle(3, 4, 5, 6, 7)
        self.assertEqual(str(r), "[Rectangle] (7) 5/6 - 3/4")

    def test_to_dictionary(self):
        r = Rectangle(4, 5, 3, 2, 6)
        expected_dict = {'id': 6, 'width': 4, 'height': 5, 'x': 3, 'y': 2}
        self.assertEqual(r.to_dictionary(), expected_dict)

    def test_update(self):
        r = Rectangle(1, 1)
        r.update(3, 4, 5, 6, 2)
        self.assertEqual(r.id, 3)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 6)
        self.assertEqual(r.y, 2)

    def test_save_to_file(self):
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_int_width(self):
        with self.assertRaises(TypeError):
            Rectangle("2", 3)

    def test_int_height(self):
        with self.assertRaises(TypeError):
            Rectangle(3, "4")

    def test_init_with_invalid_y(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 3, 4, "5")
