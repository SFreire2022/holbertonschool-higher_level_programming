#!/usr/bin/python3
"""Module containing just one function to returna a list of lists
of integers representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """that returns a list of lists of integers representing
    the Pascal’s triangle of n"""
    triangle = []
    if n == 0:
        return triangle

    triangle.append([1])

    for i in range(1, n):
        bef = triangle[-1]
        aftr = [1]
        for i in range(len(bef) - 1):
            aftr.append(bef[i] + bef[i + 1])
        aftr += [1]
        triangle.append(aftr)

    return triangle
