#!/usr/bin/python3
"""
5-text_identation.py
Module containing just one function that
prints a text with 2 new lines after each of these characters: ., ? and :

Prototype: def text_indentation(text):
text must be a string, otherwise raise a TypeError exception with the message
text must be a string
There should be no space at the beginning or at the end of each printed line
"""


def text_indentation(text):
    """
    prints a <text> with 2 new lines after each of these characters: ., ? and :
    <text> must be a string, otherwise raise a TypeError exception
    with the message:
    text must be a string
    """
    if type(text) is not str:
        raise TypeError('text must be a string')

    brk_line = ['.', '?', ':']

    for char in range(len(text)):
        if text[char] is ' ' and text[char - 1] in brk_line:
            continue
        print(text[char], end='')
        if text[char] == '.' or text[char] == '?' or text[char] == ':':
            print('', end='\n\n')
