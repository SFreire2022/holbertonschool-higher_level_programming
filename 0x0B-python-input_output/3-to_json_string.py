#!/usr/bin/python3
"""Module containing just one function to returnthe JSON representation
of an object"""
import json


def to_json_string(my_obj):
    """Function that returns the JSON representation of an object (string)"""
    return (json.dumps(my_obj))
