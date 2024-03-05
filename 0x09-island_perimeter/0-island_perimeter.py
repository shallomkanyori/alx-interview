#!/usr/bin/python3
"""Solution to the Island Perimeter problem"""


def island_perimeter(grid):
    """Returns the perimeter of the island in a grid.

    Args:
        grid (list of list of integer): The grid.

    0 is water, 1 is land. Each cell is sqaure with side length 1. Cells are
    connected horizontall/vertically. The grid is rectangular and completely
    surrounded by water. There is at most 1 island and at least 0 islands. The
    island does not have lakes.
    """

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                continue

            if r == 0 or grid[r - 1][c] == 0:
                perimeter += 1

            if r == (rows - 1) or grid[r + 1][c] == 0:
                perimeter += 1

            if c == 0 or grid[r][c - 1] == 0:
                perimeter += 1

            if c == (cols - 1) or grid[r][c + 1] == 0:
                perimeter += 1

    return perimeter
