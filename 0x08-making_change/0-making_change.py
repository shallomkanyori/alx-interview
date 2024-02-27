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

    # dp[i] == The minimum number of coins to make i
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for i in range(total + 1):
        for c in coins:
            if c > i:
                continue

            dp[i] = min(dp[i], dp[i - c] + 1)

    if dp[total] > total:
        return -1

    return dp[total]
