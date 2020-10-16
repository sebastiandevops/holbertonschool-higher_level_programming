#!/usr/bin/python3
"""Unittest for Rectangle class([..])
"""
import unittest
import inspect
import json
from models.base import Base, __doc__
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_doctstrings(self):
        """Checking docstring for Rectangle class
        """
        self.assertTrue(len(__doc__.strip()) > 0)
        self.assertTrue(len(Rectangle.__doc__.strip()) > 0)
        functions = inspect.getmembers(Rectangle, predicate=inspect.ismethod)
        for name, func in functions:
            self.assertTrue(len(func.__doc__.strip()) > 0)
        functions = inspect.getmembers(Rectangle,
                                       predicate=inspect.isfunction)
        for name, func in functions:
            self.assertTrue(len(func.__doc__.strip()) > 0)

    def test_id_none(self):
        """Test if id is none.
        """
        firstRect = Rectangle(5, 2, id=1)
        self.assertEqual(firstRect.id, 1)

    def test_nb_test(self):
        """Test if rectangle exists.
        """
        secondRect = Rectangle(1, 2)
        self.assertTrue(secondRect)

    def test_id_not_none(self):
        """Test if id is different from none.
        """
        secondRect = Rectangle(2, 10, 0, 0, 12)
        self.assertEqual(secondRect.id, 12)

    def test_string(self):
        """Test one height as a string.
        """
        with self.assertRaises(TypeError):
            Rectangle(10, "2").id

    def test_width_less_than_zero(self):
        """Test width less than zero.
        """
        r = Rectangle(10, 2, id=13)
        with self.assertRaises(ValueError):
            r.width = -10

    def test_x_diff_to_int(self):
        """Test x setter method as string
        """
        r = Rectangle(10, 2, id=14)
        with self.assertRaises(TypeError):
            r.x = {}

    def test_y_less_than_zero(self):
        """Test y as an integer less than zero.
        """
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

    def test_area_methods(self):
        """Test area method with width=3 and height=2.
        """
        rectArea = Rectangle(3, 2, id=15)
        self.assertEqual(rectArea.area(), 6)

    def test_area_methods2(self):
        """Test area method with five arguments and width=8
        and height=7.
        """
        rectArea2 = Rectangle(8, 7, 0, 0, 16)
        self.assertEqual(rectArea2.area(), 56)

    def test_display_method(self):
        """Display method with width=3, height=2.
        """
        result = "###\n###\n"
        self.assertEqual(Rectangle(3, 2, id=17).display(), result)

    def test_str_method(self):
        """Test Rectangle representation with five arguments.
        """
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 18)),
                         "[Rectangle] (18) 2/1 - 4/6")

    def test_str_method(self):
        """Test str method with three arguments: width, height and x.
        """
        self.assertEqual(str(Rectangle(5, 5, 1, id=19)),
                         "[Rectangle] (19) 1/0 - 5/5")

    def test_display_method_with_axis(self):
        """Test display method with x and y axis
        """
        r1 = Rectangle(2, 3, 2, 2, id=20)
        self.assertEqual(r1.display(), "\n\n  ##\n  ##\n  ##\n")

    def test_update_0_method(self):
        """Test args update method four arguments and then update the id.
        """
        r2 = Rectangle(10, 10, 10, 10)
        r2.update(89)
        self.assertEqual(str(r2), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_0_method_2(self):
        """Test args update method with four arguments
        and then update the id, the width.
        """
        r3 = Rectangle(10, 10, 10, 10)
        r3.update(89, 2)
        self.assertEqual(str(r3), "[Rectangle] (89) 10/10 - 2/10")

    def test_update_0_method_3(self):
        """Test args update method with four
        arguments and then update the id, the
        width and height.
        """
        r4 = Rectangle(10, 10, 10, 10)
        r4.update(89, 2, 3)
        self.assertEqual(str(r4), "[Rectangle] (89) 10/10 - 2/3")

    def test_update_0_method_3(self):
        """Test args update method with four arguments and
        then update the id, the width, height and x axis.
        """
        r5 = Rectangle(10, 10, 10, 10)
        r5.update(89, 2, 3, 4)
        self.assertEqual(str(r5), "[Rectangle] (89) 4/10 - 2/3")

    def test_update_0_method_3(self):
        """Test args update method with four arguments
        and then update the id, the width, height, x axis and y axis.
        """
        r6 = Rectangle(10, 10, 10, 10)
        r6.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r6), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_1_method(self):
        """Test kwargs update method with five arguments
        and then update height instance.
        """
        rec1 = Rectangle(10, 10, 10, 10, 10)
        rec1.update(height=1)
        self.assertEqual(str(rec1), "[Rectangle] (10) 10/10 - 10/1")

    def test_update_1_method_2(self):
        """Test kwargs update method with five arguments and
        then update width
        and x instance.
        """
        rec1 = Rectangle(10, 10, 10, 10, 10)
        rec1.update(width=1, x=2)
        self.assertEqual(str(rec1), "[Rectangle] (10) 2/10 - 1/10")

    def test_update_1_method_3(self):
        """Test kwargs update method with five arguments and
        then update width x, y instance and id.
        """
        rec1 = Rectangle(10, 10, 10, 10, 10)
        rec1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(rec1), "[Rectangle] (89) 3/1 - 2/10")

    def test_update_1_method_4(self):
        """Test kwargs update method with five arguments
        and then update width, height, x  and y instance.
        """
        rec1 = Rectangle(10, 10, 10, 10, 10)
        rec1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(rec1), "[Rectangle] (10) 1/3 - 4/2")

    def test_type_dict_representation(self):
        """Test type method return
        """
        r20 = Rectangle(10, 2, 1, 9, id=100)
        r20Dict = r20.to_dictionary()
        self.assertEqual(str(type(r20Dict)), "<class 'dict'>")

    def test_dict_representation_(self):
        """Dict representation method test.
        """
        rec2 = Rectangle(10, 2, 1, 9, id=1)
        self.assertEqual(rec2.to_dictionary(),
                         {'x': 1, 'y': 9, 'id': 1,
                          'height': 2, 'width': 10})

    def test_update_with_dict_representation(self):
        """Test update method with dict representation as argument
        """
        rec3 = Rectangle(10, 2, 1, 9, id=100)
        rec3_dictionary = rec3.to_dictionary()
        rec4 = Rectangle(1, 1, id=20)
        rec4.update(**rec3_dictionary)
        self.assertEqual(str(rec4), "[Rectangle] (100) 1/9 - 10/2")

    def test_dict_to_JSON(self):
        """test type of JSON string representation method.
        """
        r21 = Rectangle(10, 7, 2, 8, id=1)
        dictionary = r21.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(str(type(json_dictionary)), "<class 'str'>")

    def test_to_json_representation(self):
        """To json representation method test
        """
        r22 = Rectangle(10, 7, 2, 8, id=22)
        dictionary = [r22.to_dictionary()]
        json_dictionary = Base.to_json_string([dictionary])
        toCompare = [{"x": 2, "width": 10, "id": 22, "height": 7, "y": 8}]
        self.assertEqual(dictionary, toCompare)
        self.assertEqual(str(type(json_dictionary)), "<class 'str'>")

    def test_to_dictionary(self):
        """to_dictionary method test
        """
        r23 = Rectangle(3, 5, 1, id=23)
        stri = "[Rectangle] (23) 1/0 - 3/5"
        r23_dictionary = r23.to_dictionary()
        r24 = Rectangle.create(**r23_dictionary)
        self.assertFalse(r23 == r24)
        self.assertEqual(str(r23), stri)

    def test_create_method(self):
        """create method test
        """
        r26 = Rectangle.create(**{'id': 89, 'width': 1})
        stri = "[Rectangle] (89) 0/0 - 1/1"
        self.assertEqual(str(r26), stri)

    def test_create_method2(self):
        """create method test
        """
        r27 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        stri = "[Rectangle] (89) 0/0 - 1/2"
        self.assertEqual(str(r27), stri)

    def test_create_method3(self):
        """create method test
        """
        r28 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        stri = "[Rectangle] (89) 3/0 - 1/2"
        self.assertEqual(str(r28), stri)

    def test_create_method4(self):
        """create method test
        """
        r29 = Rectangle.create(**{'id': 89, 'width': 1,
                                  'height': 2, 'x': 3, 'y': 4})
        stri = "[Rectangle] (89) 3/4 - 1/2"
        self.assertEqual(str(r29), stri)


if __name__ == '__main__':
    unittest.main()
