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

    expected_length = 0

    # Try to match the length of the character based on the most significant
    # bits
    for i in range(len(data)):
        if data[i] & 0b100000000 == 0b00000000:
            expected_length = 1
        elif data[i] & 0b11100000 == 0b11000000:
            expected_length = 2
        elif data[i] & 0b11110000 == 0b11100000:
            expected_length = 3
        elif data[i] & 0b11111000 == 0b11110000:
            expected_length = 4
        elif data[i] & 0b11111100 == 0b11111000:
            expected_length = 5
        elif data[i] & 0b11111110 == 0b11111100:
            expected_length = 6
        else:
            return False

        expected_length -= 1
        while expected_length > 0:
            i += 1

            if i >= len(data):
                return False

            if data[i] & 0b11000000 != 0b10000000:
                return False

    return True
