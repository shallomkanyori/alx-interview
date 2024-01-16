#!/usr/bin/python3
"""Minimum operations

Functions:
    minOperations(n)
"""


def minOperations(n: int) -> int:
    """Solves the minimum operations problem.

    In a text file, there is a single character H. Your text editor can execute
    only two operations in this file: Copy All and Paste. Given a number n,
    calculate the fewest number of operations needed to result in exactly n H
    characters in the file.
    """

    if not isinstance(n, int):
        raise TypeError("N must be an int")

    if n <= 2:
        return 0

    ops = 0
    root = 2
    while root <= n:
        if n % root == 0:
            ops += root
            n /= root
            root -= 1
        root += 1

    return ops
