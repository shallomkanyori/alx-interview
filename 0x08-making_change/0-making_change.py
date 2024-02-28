#!/usr/bin/python3
"""Coin Change Solution

Functions:
    makeChange(coins, total)
"""


def makeChange(coins, total):
    """Returns the minimum number of coins to make up total given coins.

    Args:
        coins (list of int): The values of the coins in possession.
        total (int): The value to make up.
    """

    if total <= 0:
        return 0

    i = 0
    res = 0
    rem = total
    n = len(coins)
    coins_sorted = sorted(coins, reverse=True)

    while rem > 0:
        if i >= n:
            return -1

        if rem - coins_sorted[i] >= 0:
            rem -= coins_sorted[i]
            res += 1
        else:
            i += 1

    return res
