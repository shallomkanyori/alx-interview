#!/usr/bin/python3
"""Log Parsing

A script that reads stdin line by line and copmutes metrics.

Input format:
    <IPAddress> - [<date>] "GET /projects/260 HTTP/1.1" <statuscode> <filesize>
    (Any line that does not match this format is skipped)

Every 10 lines and/or a keyboard interruption, these statistics are printed:
    Total file size (sum of all previous <file size>: File size <total size>
    Status code frequency:
        Possible status codes: [200, 301, 400, 401, 403, 404, 405, 500]
        Any status code that doesn't appear or is not an integer is not printed
        Format: <status code>: <frequency>
        Status codes are printed in ascending order
"""
import sys
import re


def print_stats(total_size, codes):
    """Prints the specified stats.

    Args:
        total_size (int): The sum of the file sizes so far.
        codes: The status codes fequencies.
    """

    print("File size: {}".format(total_size))

    for k in sorted(codes.keys()):
        if codes[k] > 0:
            print("{}: {}".format(k, codes[k]))


if __name__ == "__main__":
    lines = 0
    total_size = 0
    codes = {"200": 0, "301": 0, "400": 0, "401": 0,
             "403": 0, "404": 0, "405": 0, "500": 0}

    line_format = (r'^\d+\.\d+\.\d+\.\d+ - \[.*?\] '
                   r'"GET /projects/260 HTTP/1.1" '
                   r'(\d+) (\d+)$')

    try:
        for line in sys.stdin:
            m = re.match(line_format, line)

            if not m:
                continue

            total_size += int(m[2])

            codes[m[1]] += 1

            lines += 1
            if lines % 10 == 0:
                print_stats(total_size, codes)

    except KeyboardInterrupt:
        print_stats(total_size, codes)
        raise
