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

    if n <= 0:
        return 0

    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        # Calculate min operations to i from its factors
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j, dp[i // j] + j)

    return int(dp[n])
