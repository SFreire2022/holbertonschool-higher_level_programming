#!/usr/bin/python3
"""Module containing just one class definition for Models"""


class Base:
    """Class Model definition
    Private class atributes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Public class instance constructor
        Inicilizating atributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
