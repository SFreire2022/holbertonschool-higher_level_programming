#!/usr/bin/python3
"""Module including a class definition"""


class MyList(list):
    """Class MyList inherited from list"""

    def print_sorted(self):
        """Method that prints the list sorted"""
        print(sorted(self))
