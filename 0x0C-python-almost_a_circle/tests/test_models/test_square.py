import unittest
from models.square import Square

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

    def test_negative_size(self):
        with self.assertRaises(ValueError):
            Square(-1)
if __name__ == '__main__':
    unittest.main()
