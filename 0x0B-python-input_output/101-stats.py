#!/usr/bin/python3
import sys

def print_metrics(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))

def parse_line(line, total_size, status_codes):
    try:
        parts = line.split()
        size = int(parts[-1])
        status_code = parts[-2]
        total_size += size
        status_codes[status_code] = status_codes.get(status_code, 0) + 1
        return total_size, status_codes
    except Exception as e:
        return total_size, status_codes
