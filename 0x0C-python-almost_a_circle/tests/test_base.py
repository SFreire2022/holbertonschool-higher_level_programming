#!/usr/bin/python3
""" Unittest for all the methods of the class Base
Check pycodestyle "PEP8" for the complete module """
import unittest
import pycodestyle
from models.base import Base


class TestBaseModule(unittest.TestCase):
    """ A class to test Base Module """
    def test_pycodestyle_pep8(self):
        """ Style code meets PEP8 """
        style = pycodestyle.StyleGuide(quit=True)
        check = style.check_files(['models/base.py'])
        self.assertEqual(
            check.total_errors, 0,
            'PEP8 style errors: %d' % check.total_errors)

    def test_empty_and_none_id(self):
        """ Empty and None Base Class id """
        base_inst = Base()
        self.assertEqual(base_inst.id, 1)
        base_inst = Base(None)
        self.assertEqual(base_inst.id, 2)

    def test_positive_id(self):
        """ Positive Base Class id """
        base_inst = Base(10)
        self.assertEqual(base_inst.id, 10)
        base_inst = Base(1000)
        self.assertEqual(base_inst.id, 1000)

    def test_negative_id(self):
        """ Negative Base Class id """
        base_inst = Base(-10)
        self.assertEqual(base_inst.id, -10)
        base_inst = Base(-1000)
        self.assertEqual(base_inst.id, -1000)
