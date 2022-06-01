#!/usr/bin/python3
"""Module containing just one class definition for Student"""


class Student:
    """Class Student definition"""

    def __init__(self, first_name, last_name, age):
        """Public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method that retrieves a dictionary
        representation of a Student instance """
        if attrs is not None:
            dictionary = {}
            for atrib in attrs:
                if atrib in self.__dict__:
                    dictionary[atrib] = self.__dict__[atrib]
            return dictionary
        return self.__dict__
