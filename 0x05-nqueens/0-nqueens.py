#!/usr/bin/python3
"""N Queens

Functions:
    nqueens(n, row, cols, diags+, diags-)
"""
import sys


def nqueens(n, i, a, b, c):
    """Returns all the solutions to the N queens problem.

    The N queens puzzle is the challenge of placing N non-attacking queens on
    an NxN chessboard.

    Args:
        n(int): The size of the chessboard.
        i(int): The current row being considered.
        a(list of int): The columns that are not safe.
        b(list of int): The unsafe top-left to bottom-right diagonals.
        c(list of int): The unsafe top-right to bottom-left diagonals.
    """
    if i < n:
        for j in range(n):
            if j not in a and i+j not in b and i-j not in c:
                yield from nqueens(n, i + 1, a+[j], b+[i+j], c+[i-j])
    else:
        yield a


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    for s in nqueens(n, 0, [], [], []):
        solution = [[i, j] for i, j in enumerate(s)]
        print(solution)
