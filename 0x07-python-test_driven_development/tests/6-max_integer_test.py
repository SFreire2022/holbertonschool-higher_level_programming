#!/usr/bin/python3
"""
Unittest for max_integer([..])
Module to find the max integer in a list
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ Define methods for test different cases """

    def test_normal(self):
        """ Normal mode list with 2 or more values """
        self.assertEqual(max_integer([1, 8]), 8)

    def test_one(self):
        """ One single value in a list """
        self.assertEqual(max_integer([12]), 12)

    def test_repeated(self):
        """ Repeated max values """
        self.assertEqual(max_integer([1, 4, 2, 4]), 4)

    def test_negative(self):
        """ Bigger negative values """
        self.assertEqual(max_integer([-1, -2, -8]), -1)

    def test_float(self):
        """ Bigger float value """
        self.assertEqual(max_integer([10.1, 2.5, 1.7, 2.4]), 2.5)
        self.assertEqual(max_integer([-10.1, -2.5, -1.7, -2.4]), -1.7)


    def test_string(self):
        """ Bigger char and string decimal value """
        self.assertEqual(max_integer(["aaab", "aaaz"]), "aaaz")
        self.assertEqual(max_integer(["asab", "Asaz"]), "asab")
        self.assertEqual(max_integer(["e", "g"]), "g")

    def test_bool(self):
        """ Bigger boolean value """
        self.assertEqual(max_integer([False, True]), True)
        self.assertEqual(max_integer([False, False]), False)
        self.assertEqual(max_integer([True, False]), True)
        self.assertEqual(max_integer([True, True]), True)
        self.assertEqual(max_integer([1, False]), 1)

    def test_matrix(self):
        """ Max list value in a list of lists (matrix) """
        self.assertEqual(max_integer([[1, 2], [2, 3]]), [2, 3])
        self.assertEqual(max_integer([(1, 2), (2, 3)]), (2, 3))

    def test_empty(self):
        """ Empty values return None """
        self.assertIsNone(max_integer([]))
        self.assertEqual(max_integer({}), None)
        self.assertEqual(max_integer(()), None)

    def test_none(self):
        """ list with one None element """
        self.assertRaises(TypeError, max_integer, [None, None])

    def test_mix(self):
        """ mixed data type list must raise TypeError """
        self.assertRaises(TypeError, max_integer, [1, 'str', True])
        self.assertRaises(TypeError, max_integer, [1, [2, 3], True])
        self.assertRaises(TypeError, max_integer, [1, [2, 3], {4, 5}])
        self.assertRaises(TypeError, max_integer, [1, (2, 3), None])

    def test_one_number(self):
        """ Pass a number instead of list value mas raise TypeError """
        self.assertRaises(TypeError, max_integer, 1)
        self.assertRaises(TypeError, max_integer, 1.1)
