#!/usr/bin/python3
"""Module containing just one function to return an object
(Python data structure) represented by JSON string"""
import json


def from_json_string(my_str):
    """Function that returns an object
    represented by a JSON string."""
    return (json.loads(my_str))
