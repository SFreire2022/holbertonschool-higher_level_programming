#!/usr/bin/python3
""" Unittest for all the methods of the class Rectangle
Check pycodestyle "PEP8" for the complete module """
import unittest
import pycodestyle
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO



class TestRectangleModule(unittest.TestCase):
    """ A class to test Rectangle Module """

    def test_pycodestyle_pep8(self):
        """ Style code meets PEP8 """
        style = pycodestyle.StyleGuide(quit=True)
        check = style.check_files(['models/rectangle.py'])
        self.assertEqual(
            check.total_errors, 0,
            'PEP8 style errors: %d' % check.total_errors)

    def test_id_default(self):
        """ Base Class id inherited in Rectangle instance """
        r1 = Rectangle(8, 6)
        r1.id = 1
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(7, 20)
        r2.id = 2
        self.assertEqual(r2.id, 2)

    def test_rectangle_instance(self):
        """ Rectangle is instance of Base ? """
        r = Rectangle(30, 25, 10, 10, 3)
        self.assertEqual(type(r), Rectangle)
        self.assertTrue(type(r) == Rectangle)
        self.assertFalse(type(r) == Base)
        self.assertTrue(isinstance(r, Base))
        self.assertTrue(isinstance(r, Rectangle))

    def test_set_id(self):
        """ Set specific id """
        r3 = Rectangle(3, 8, 1, 2, 100)
        self.assertEqual(r3.id, 100)

    def test_wrong_args(self):
        """ Wrong argumments """
        with self.assertRaises(TypeError):
            r4 = Rectangle(8)
        with self.assertRaises(TypeError):
            r4 = Rectangle(12, 5, 10, 10, 100, 1)

    def test_correct_args(self):
        """ Correct argumments (normal function) """
        r5 = Rectangle(15, 3, 10, 20, 15)
        self.assertEqual(r5.width, 15)
        self.assertEqual(r5.height, 3)
        self.assertEqual(r5.x, 10)
        self.assertEqual(r5.y, 20)
        self.assertEqual(r5.id, 15)

    def test_args_type_error(self):
        """ Not integer argumments """
        r6 = Rectangle(10, 20)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r6.width = "string10"
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r6.height = "string20"
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r6.x = "string1"
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r6.y = "string2"

    def test_width_height_gt_0(self):
        """ Width and height greater than 0 """
        r7 = Rectangle(10, 20)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r7.width = -1
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r7.height = 0

    def test_x_y_ge_0(self):
        """ x or y greater equal 0 """
        r8 = Rectangle(10, 20)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r8.x = -3
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r8.y = -2

    def test_area(self):
        """ test area """
        r9 = Rectangle(5, 10)
        self.assertEqual(r9.area(), 50)
        r9.height = 3
        self.assertEqual(r9.area(), 15)

    def test_display(self):
        """ Display Rectangle instance with valid args
        Taking care of xy position"""
        r10 = Rectangle(2, 3, 3, 2)
        with patch('sys.stdout', new=StringIO()) as f_stdo:
             r10.display()
             self.assertEqual(f_stdo.getvalue(), "\n\n   ##\n   ##\n   ##\n")
        """ Display Rectangle instance with invalid args """
        with self.assertRaises(ValueError):
            r11 = Rectangle(-10, 0, -2, 10)
            r11.display()

    def test_str_repr(self):
        """ Valid string representation for the instance """
        r12 = Rectangle(2, 4, 3, 6, 12)
        with patch('sys.stdout', new=StringIO()) as f_stdo:
            self.assertEqual(f_stdo.getvalue(), "[Rectangle] (12) 3/6 - 2/4")
        r13 = Rectangle(6, 3, 1, 3, 13)
        with patch('sys.stdout', new=StringIO()) as f_stdo:
            self.assertEqual(f_stdo.getvalue(), "[Rectangle] (13) 1/3 - 6/3")
