import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_init(self):
        b = Base()
        self.assertIsInstance(b, Base)

    def test_init_with_id(self):
         b = Base(8)
         self.assertEqual(b.id, 8)

    def test_init_with_negative_id(self):
        with self.assertRaises(ValueError):
            b = Base(-8)

    def test_to_json_string(self):
        b = Base()
        self.assertEqual(Base.to_json_string([{'id': 1}]), '[{"id": 1}]')
        self.assertEqual(Base.to_json_string([{'id': 2}]), '[{"id": 2}]')

    def test_from_json_string(self):
        b = Base()
        self.assertEqual(Base.from_json_string('[{"id": 1}]'), [{'id': 1}])
        self.assertEqual(Base.from_json_string('[{"id": 2}]'), [{'id': 2}])

if __name__ == '__main__':
    unittest.main()
