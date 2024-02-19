#!/usr/bin/python3
"""Solution to rotation a square matrix clockwise

Functions:
    rotate_2d_matrix(matrix)
"""


def rotate_2d_matrix(matrix):
    """Rotates a sqauare matrix 90 degrees clockwise"""

    n = len(matrix)

    # transpose matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse each row
    for row in matrix:
        row.reverse()
