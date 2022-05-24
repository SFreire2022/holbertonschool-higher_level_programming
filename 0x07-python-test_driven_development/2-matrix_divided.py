#!/usr/bin/python3
"""
This library is very simple, since it only has one function called
'matrix_divided()'.
Prototype: 'def matrix_divided(matrix, div):'
* matrix and div must be integers or floats, otherwise raise a
TypeError exception with their asociated message.
* Return new matrix with his elements dvided by div.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix
    matrix must be a list of lists of integers or floats
    Every row of the matrix must be of the same size
    div must be a number (integer or float) not 0
    Returns a new matrix with element divided by div
    """

    res_mtx = []
    cel = 0
    m_error = 'matrix must be a matrix (list of lists) of integers/floats'

    if type(div) not in [int, float]:
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError(m_error)
        for j in matrix[i]:
            if type(j) not in [int, float]:
                raise TypeError(m_error)

    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError(m_error)
        if len(matrix[0]) != len(matrix[i]):
            raise TypeError('Each row of the matrix must have the same size')

    for i in range(len(matrix)):
        res_mtx.append([])
        for j in matrix[i]:
            cel = j / div
            cel = round(cel, 2)
            res_mtx[i].append(cel)
    return res_mtx
