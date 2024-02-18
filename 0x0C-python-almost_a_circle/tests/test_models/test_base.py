import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):
    def test_init(self):
        b = Base()
        self.assertIsInstance(b, Base)

    def test_init_with_id(self):
         b = Base(4)
         self.assertEqual(b.id, 4)

    def test_init_with_negative_id(self):
        with self.assertRaises(ValueError):
            b = Base(-8)

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_nb_objects_increment(self):
        obj1 = Base()
        self.assertEqual(Base._Base__nb_objects, 1)
        obj2 = Base()
        self.assertEqual(Base._Base__nb_objects, 2)

    def test_to_json_string(self):
        b = Base()
        self.assertEqual(Base.to_json_string([{'id': 1}]), '[{"id": 1}]')
        self.assertEqual(Base.to_json_string([{'id': 2}]), '[{"id": 2}]')

    def test_from_json_string(self):
        b = Base()
        self.assertEqual(Base.from_json_string('[{"id": 1}]'), [{'id': 1}])
        self.assertEqual(Base.from_json_string('[{"id": 2}]'), [{'id': 2}])

    def test_create(self):
        r1 = Rectangle(3, 5, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertFalse(r1 is r2)
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())

    def test_load_from_file(self):
        r1 = Rectangle(5, 5)
        r2 = Rectangle(10, 10)
        Rectangle.save_to_file([r1, r2])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 2)
        self.assertIsInstance(rectangles[0], Rectangle)
        self.assertIsInstance(rectangles[1], Rectangle)

if __name__ == '__main__':
    unittest.main()
