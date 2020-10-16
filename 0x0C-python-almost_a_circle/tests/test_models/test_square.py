#!/usr/bin/python3
"""Unittest for Square class([..])
"""
import unittest
import inspect
from models.rectangle import Rectangle, __doc__
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_doctstrings(self):
        """Checking docstring for Square class
        """
        self.assertTrue(len(__doc__.strip()) > 0)
        self.assertTrue(len(Square.__doc__.strip()) > 0)
        functions = inspect.getmembers(Square, predicate=inspect.ismethod)
        for name, func in functions:
            self.assertTrue(len(func.__doc__.strip()) > 0)
        functions = inspect.getmembers(Square,
                                       predicate=inspect.isfunction)
        for name, func in functions:
            self.assertTrue(len(func.__doc__.strip()) > 0)

    def test_id(self):
        """Test if id is none.
        """
        firstSquare = Square(5, 2, 2, id=1)
        self.assertEqual(firstSquare.id, 1)

    def test_area_methods(self):
        """Area method test
        """
        s2 = Square(5)
        self.assertEqual(s2.area(), 25)

    def test_display_method(self):
        """Display method test.
        """
        s3 = Square(2, 2)
        self.assertEqual(s3.display(), "  ##\n  ##\n")

    def test_getter_size(self):
        """Getter size method test.
        """
        s4 = Square(5)
        self.assertEqual(s4.size, 5)

    def test_setter_size(self):
        """Setter size method test.
        """
        s5 = Square(5)
        s5.size = 10
        self.assertEqual(s5.size, 10)

    def test_print_square(self):
        """__str__ method test
        """
        s6 = Square(3, 1, 3, 10)
        self.assertEqual(str(s6), "[Square] (10) 1/3 - 3")

    def test_update_1(self):
        """Update args method test - id update.
        """
        s7 = Square(5, 0, 0, id=100)
        s7.update(10)
        self.assertEqual(str(s7), "[Square] (10) 0/0 - 5")

    def test_update_2(self):
        """Update args method test - size and id update
        """
        s8 = Square(5, 0, 0, id=100)
        s8.update(1, 2)
        self.assertEqual(str(s8), "[Square] (1) 0/0 - 2")

    def test_update_3(self):
        """Update args method test - size, x axis and id update.
        """
        s9 = Square(5, 0, 0, id=100)
        s9.update(1, 2, 3)
        self.assertEqual(str(s9), "[Square] (1) 3/0 - 2")

    def test_update_4(self):
        """Update args method test - size, x and y axis and id update.
        """
        s10 = Square(5, 0, 0, id=100)
        s10.update(1, 2, 3, 4)
        self.assertEqual(str(s10), "[Square] (1) 3/4 - 2")

    def test_update_5(self):
        """Update kwargs method test - x axis update.
        """
        s11 = Square(5, 0, 0, id=100)
        s11.update(x=12)
        self.assertEqual(str(s11), "[Square] (100) 12/0 - 5")

    def test_update_6(self):
        """Update kwargs method test - y axis and size update.
        """
        s12 = Square(5, 0, 0, id=100)
        s12.update(size=7, y=1)
        self.assertEqual(str(s12), "[Square] (100) 0/1 - 7")

    def test_update_7(self):
        """Update kwargs method test - id, y axis and size update.
        """
        s13 = Square(5, 0, 0, id=100)
        s13.update(size=7, id=89, y=1)
        self.assertEqual(str(s13), "[Square] (89) 0/1 - 7")

    def test_dict_representation_type(self):
        """Dict representation method test type.
        """
        s14 = Square(10, 2, 1, id=1)
        s14Dict = s14.to_dictionary()
        self.assertEqual(str(type(s14Dict)), "<class 'dict'>")

    def test_dict_representation_print(self):
        """Dict representation method test print.
        """
        s15 = Square(10, 2, 1, id=1)
        self.assertEqual(s15.to_dictionary(),
                         {'id': 1, 'x': 2, 'size': 10, 'y': 1})

    def test_dict_representation_update(self):
        """Update attribute with dictionary as argument of update method.
        """
        s15 = Square(10, 2, 1, id=1)
        s15Dict = s15.to_dictionary()
        s16 = Square(1, 1, id=50)
        s16.update(**s15Dict)
        self.assertEqual(str(s16), "[Square] (1) 2/1 - 10")

    def test_to_dictionary(self):
        """to_dictionary method test
        """
        s17 = Square.create(**{'id': 89})
        stri = "[Square] (89) 0/0 - 1"
        self.assertEqual(str(s17), stri)

    def test_to_dictionary_2(self):
        """to_dictionary method test
        """
        s18 = Square.create(**{'id': 89, 'size': 1})
        stri = "[Square] (89) 0/0 - 1"
        self.assertEqual(str(s18), stri)

    def test_to_dictionary_3(self):
        """to_dictionary method test
        """
        s19 = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        stri = "[Square] (89) 2/0 - 1"
        self.assertEqual(str(s19), stri)

    def test_to_dictionary_4(self):
        """to_dictionary method test
        """
        s20 = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        stri = "[Square] (89) 2/3 - 1"
        self.assertEqual(str(s20), stri)

    def test_square_with_string_attribute(self):
        """errors test
        """
        with self.assertRaises(TypeError):
            Square("1")

    def test_square_with_string_attribute2(self):
        """errors test
        """
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_square_with_string_attribute3(self):
        """errors test
        """
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_square_with_value_errors(self):
        """errors test
        """
        with self.assertRaises(ValueError):
            Square(-1)

    def test_square_with_value_errors2(self):
        """errors test
        """
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_square_with_value_errors3(self):
        """errors test
        """
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_square_with_value_errors4(self):
        """errors test
        """
        with self.assertRaises(ValueError):
            Square(0)


if __name__ == '__main__':
    unittest.main()
