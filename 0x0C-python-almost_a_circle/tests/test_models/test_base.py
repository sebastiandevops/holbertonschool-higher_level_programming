#!/usr/bin/python3
"""Unittest for base class([..])
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_id_none(self):
        """Test if id is none."""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id_not_none(self):
        """Test if id is different from none."""
        b2 = Base(12)
        self.assertEqual(b2.id, 12)


if __name__ == '__main__':
    unittest.main()
