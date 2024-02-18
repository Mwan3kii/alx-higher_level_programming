import unittest
from models.square import Square
from unittest.mock import patch
import io

class TestSquare(unittest.TestCase):
    def test_init(self):
        s = Square(6, 3, 2, 1)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 6)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 2)

    def test_str(self):
        s = Square(3, 4, 5, 6)
        self.assertEqual(str(s), "[Square] (6) 4/5 - 3")

    def test_area(self):
        s = Square(6)
        self.assertEqual(s.area(), 36)

    def test_to_dictionary(self):
        s = Square(4, 3, 5, 2)
        expected_dict = {'id': 2, 'size': 4, 'x': 3, 'y': 5}
        self.assertEqual(s.to_dictionary(), expected_dict)

    def test_size_type(self):
        with self.assertRaises(TypeError):
            Square("test")

    def test_x(self):
        with self.assertRaises(TypeError):
            Square(1, "test")

    def test_y(self):
        with self.assertRaises(TypeError):
            Square(1, 1, "test")

    def test_negative_size(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_update(self):
        s = Square(1)
        s.update(2, 3, 4, 5)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 5)

    def test_display(self):
        s = Square(3)
        expected_output = "###\n###\n###\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            s.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)
    def test_create(self):
        s1_dict = {'id': 1, 'size': 5}
        s2_dict = {'id': 2, 'size': 10}
        s1 = Square.create(**s1_dict)
        s2 = Square.create(**s2_dict)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s2.size, 10)

if __name__ == '__main__':
    unittest.main()
