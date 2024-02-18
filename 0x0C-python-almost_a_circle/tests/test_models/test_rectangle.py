import unittest
from models.rectangle import Rectangle
from unittest.mock import patch
import io

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

    def test_height_setter(self):
        r = Rectangle(10, 20)
        r.height = 25
        self.assertEqual(r.height, 25)
        with self.assertRaises(ValueError):
            r.height = 0

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
