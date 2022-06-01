#!/usr/bin/python3
"""Module containing just one function that writes JSON representation
of a given object to a given file"""
import json


def save_to_json_file(my_obj, filename):
    """Function that writes an Object to a text file,
    using a JSON representation."""
    with open(filename, 'w') as myfile:
        json.dump(my_obj, myfile)
