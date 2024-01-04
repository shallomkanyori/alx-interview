#!/usr/bin/python3
"""This module contains the pascal_triangle function."""


def pascal_triangle(n):
    """Returns a list of lists of integers of Pascal's triangle of n."""
    if n <= 0:
        return []

    res = []

    for i in range(n):
        row = [1 if j == 0 or j == i else res[i - 1][j - 1] + res[i - 1][j]
               for j in range(i + 1)]

        res.append(row)

    return res
