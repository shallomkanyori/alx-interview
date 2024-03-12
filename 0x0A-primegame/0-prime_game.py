#!/usr/bin/python3
"""Solution for Prime game"""


def isWinner(x, nums):
    """Returns the winner of the prime game.

    Args:
        x (int): The number of rounds played.
        nums (list of int): The end of the number range for each round.
    """

    if x <= 0:
        return None

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

    if ben == maria:
        return None

    if maria > ben:
        return 'Maria'

    return 'Ben'
