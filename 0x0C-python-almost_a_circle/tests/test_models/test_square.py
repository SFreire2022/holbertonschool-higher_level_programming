#!/usr/bin/python3
""" Unittest for all the methods of the class Rectangle
Check pycodestyle "PEP8" for the complete module """
import unittest
import pycodestyle
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from unittest.mock import patch
from io import StringIO



class TestSquareModule(unittest.TestCase):
    """ A class to test Square Module """

    def test_pycodestyle_pep8(self):
        """ Style code meets PEP8 """
        style = pycodestyle.StyleGuide(quit=True)
        check = style.check_files(['models/square.py'])
        self.assertEqual(
            check.total_errors, 0,
            'PEP8 style errors: %d' % check.total_errors)

    def test_id_default(self):
        """ Base Class id inherited in Square instance """
        s1 = Square(8, 6)
        s1.id = 1
        self.assertEqual(s1.id, 1)
        s2 = Square(7, 20)
        s2.id = 2
        self.assertEqual(s2.id, 2)

    def test_square_instance(self):
        """ Square is instance of Base and Rectangle ? """
        s = Square(30, 10, 10, 3)
        self.assertEqual(type(s), Square)
        self.assertTrue(type(s) == Square)
        self.assertFalse(type(s) == Base)
        self.assertTrue(isinstance(s, Base))
        self.assertTrue(isinstance(s, Rectangle))
        self.assertTrue(isinstance(s, Square))

    def test_set_id(self):
        """ Set specific id """
        s3 = Square(3, 1, 2, 100)
        self.assertEqual(s3.id, 100)

    def test_wrong_args(self):
        """ Wrong argumments """
        with self.assertRaises(TypeError):
            s4 = Square(12, 5, 10, 10, 100, 1)

    def test_correct_args(self):
        """ Correct argumments (normal function) """
        s4 = Square(8)
        self.assertEqual(s4.size, 8)
        self.assertEqual(s4.x, 0)
        self.assertEqual(s4.y, 0)
        self.assertEqual(s4.id, 12)
        s5 = Square(15, 10, 20, 15)
        self.assertEqual(s5.size, 15)
        self.assertEqual(s5.x, 10)
        self.assertEqual(s5.y, 20)
        self.assertEqual(s5.id, 15)

    def test_args_type_error(self):
        """ Not integer argumments check from inherited setter method """
        s6 = Square(10, 20)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s6.size = "string10"
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s6.x = "string1"
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s6.y = "string2"

    def test_size_gt_0(self):
        """ Size greater than 0 an check from inherited setter method """
        s7 = Square(10, 20)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s7.size = -1
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s7.size = 0

    def test_x_y_ge_0(self):
        """ x or y greater equal 0 """
        s8 = Square(10, 20)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s8.x = -3
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s8.y = -2

    def test_area(self):
        """ test area """
        s9 = Square(5)
        self.assertEqual(s9.area(), 25)
        s9.size = 3
        self.assertEqual(s9.area(), 9)

    def test_display(self):
        """ Display Square instance with valid args to stdout
        Taking care of xy position"""
        s10 = Square(2, 3, 2)
        with patch('sys.stdout', new=StringIO()) as f_stdo:
             s10.display()
             self.assertEqual(f_stdo.getvalue(), "\n\n   ##\n   ##\n")
        """ Display Square instance with invalid args """
        with self.assertRaises(ValueError):
            s11 = Square(-10, 0, -2, 10)
            s11.display()

    def test_str_repr(self):
        """ Valid string representation for the instance """
        s12 = Square(2, 3, 6, 12)
        self.assertEqual(str(s12), "[Square] (12) 3/6 - 2")
        s13 = Square(6, 1, 3, 13)
        self.assertEqual(str(s13), "[Square] (13) 1/3 - 6")

    def test_update(self):
        """ update method args and kwargs """
        s14 = Square(2, 8, 0, 18)
        """ update using first arg (id) """
        s14.update(1)
        self.assertEqual(s14.size, 2)
        self.assertEqual(s14.x, 8)
        self.assertEqual(s14.y, 0)
        self.assertEqual(s14.id, 1)
        """ update all using kwargs in different order """
        s14.update(y=7, x=9, id=18, size=11)
        self.assertEqual(s14.size, 11)
        self.assertEqual(s14.x, 9)
        self.assertEqual(s14.y, 7)
        self.assertEqual(s14.id, 18)
        """ update all using kwargs and extra atributes """
        s14.update(y=5, x=4, id=19, size=5, extra1=6, extra2=8)
        self.assertEqual(s14.size, 5)
        self.assertEqual(s14.x, 4)
        self.assertEqual(s14.y, 5)
        self.assertEqual(s14.id, 19)
