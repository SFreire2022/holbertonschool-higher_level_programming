#!/usr/bin/python3
"""Module containing just one function to print the content of the given file"""


def read_file(filename=""):
    """Function that reads a txt file using UTF8 conding and print to stdo"""
    with open(filename, encoding="utf-8") as myfile:
        filecontent = myfile.read()
        print(filecontent, end='')
