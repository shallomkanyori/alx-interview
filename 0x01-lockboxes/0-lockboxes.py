#!/usr/bin/python3
"""Module: Lockboxes

Functions:
        canUnlockAll
"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be open.

    Args:
        boxes: list of boxes which are lists of keys.

    Returns: True if all boxes can be opened. False otherwise.
    """

    n = len(boxes)
    open_boxes = [0] * n
    keys = set()

    keys.add(0)

    while keys:
        b = keys.pop()

        if open_boxes[b]:
            continue

        for k in boxes[b]:
            if k < n:
                keys.add(k)

        open_boxes[b] = 1

    return all(open_boxes)
