#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_equal(self):
        """Test if element of the list are equal."""
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_none(self):
        """Test if empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_char(self):
        """Test if list elements are character characters."""
        self.assertEqual(max_integer(["a", "b", "c"]), "c")