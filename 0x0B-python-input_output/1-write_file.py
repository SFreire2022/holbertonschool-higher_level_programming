#!/usr/bin/python3
"""Module containing just one function to write given string to the given file"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file using UTF8 coding.
    Returns the number of characters written."""
    with open(filename, 'w', encoding="utf-8") as myfile:
        return(myfile.write(text))
