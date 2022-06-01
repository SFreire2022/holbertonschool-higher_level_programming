#!/usr/bin/python3
"""Module containing just one funtion that returns the dictionary description
with simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object"""


def class_to_json(obj):
    """Funtion that returns the dictionary description
    with simple data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object"""
    return obj.__dict__
