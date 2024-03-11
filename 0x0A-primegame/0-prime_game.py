#!/usr/bin/python3
"""Solution for Prime game

Prime game:
Maria and Ben are playing a game. Given a set of consecutive integers starting
from 1 up to and including n, they take turns choosing a prime number from the
set and removing that number and its multiples from the set. The player that
cannot make a move loses the game.
They play x rounds of the game, where n may be different for each round.
Assuming Maria always goes first and both players play optimally, determine
who the winner of each game is.
"""


def isWinner(x, nums):
    """Returns the winner of the prime game.

    Args:
        x (int): The number of rounds played.
        nums (list of int): The array of n for each round(see description).
    """

    maria = 0
    ben = 0

    # sieve of erastothenes with the largest n to be played
    n_max = max(nums)
    sieve = [0] * (n_max + 1)
    sieve[0] = sieve[1] = -1

    # sieve[i] == 1 if i is prime, -1 is i is not prime
    for i in range(2, n_max + 1):
        if sieve[i] == -1:
            continue

        # Mark i as prime. Mark multiples of i as not prime numbers
        sieve[i] = 1
        for f in range(i * 2, n_max + 1, i):
            sieve[f] = -1

    for r in range(x):
        n = nums[r]

        # every prime number in range [1, n] is a move (Optimal move would be
        # prime number with greatest number of multiples)
        primes = [sieve[i] for i in range(1, n + 1) if sieve[i] != -1]

        if len(primes) % 2 == 0:
            # Ben wins if no moves at the start of the round or number of
            # available moves is even.
            ben += 1
        else:
            maria += 1
        print(f"{sieve=}\n{primes=}\n{ben=},{maria=}\n")

    if ben == maria:
        return None

    if maria > ben:
        return 'Maria'

    return 'Ben'
