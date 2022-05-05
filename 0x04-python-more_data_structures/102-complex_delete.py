#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, val in dict(a_dictionary).items():
        if value is val:
            a_dictionary.pop(key)
    return a_dictionary
