#!/usr/bin/python3
"""Module containing just one function to append given string to the given file"""


def append_write(filename="", text=""):
    """Function that appends a string to a text file using UTF8 coding.
    Returns the number of characters added."""
    with open(filename, 'a', encoding="utf-8") as myfile:
        return(myfile.write(text))
