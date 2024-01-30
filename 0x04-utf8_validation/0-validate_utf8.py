#!/usr/bin/python3
"""UTF-8 Validation

Functions:
    validUTF8(data)
"""


def validUTF8(data):
    """Determines if a given data set represent a valid UTF-8 encoding.

    Args:
        data (list of int): The data set.
    """

    if (not type(data) is list or
            not all(type(x) is int for x in data)):
        return False

    count = 0

    # Try to match the length of the character based on the most significant
    # bits
    for i in data:
        if count == 0:
            if i >> 5 == 0b110 or i >> 5 == 0b1110:
                count = 1
            elif i >> 4 == 0b1110:
                count = 2
            elif i >> 3 == 0b11110:
                count = 3
            elif i >> 7 == 0b1:
                return False
        else:
            if i >> 6 != 0b10:
                return False

            count -= 1

    return count == 0
