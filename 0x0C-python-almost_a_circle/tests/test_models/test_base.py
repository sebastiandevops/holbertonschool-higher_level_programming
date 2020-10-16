#!/usr/bin/python3
"""Unittest for base class([..])
"""
import unittest
import inspect
from models.base import Base, __doc__


class TestBase(unittest.TestCase):

    def test_doctstrings(self):
        """Checking docstring for base class
        """
        self.assertTrue(len(__doc__.strip()) > 0)
        self.assertTrue(len(Base.__doc__.strip()) > 0)
        functions = inspect.getmembers(Base, predicate=inspect.ismethod)
        for name, func in functions:
            self.assertTrue(len(func.__doc__.strip()) > 0)
        functions = inspect.getmembers(Base, predicate=inspect.isfunction)
        for name, func in functions:
            self.assertTrue(len(func.__doc__.strip()) > 0)

    def test_id_none(self):
        """Test if id is none."""
        b1 = Base(id=1)
        self.assertEqual(b1.id, 1)

    def test_id_not_none(self):
        """Test if id is different from none."""
        b2 = Base(12)
        self.assertEqual(b2.id, 12)

    def test_base_class(self):
        """Test base class
        """
        b3 = Base()
        self.assertEqual(Base._Base__nb_objects, 1)


if __name__ == '__main__':
    unittest.main()
