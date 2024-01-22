#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as e:
        error_message = f"Exception: {e}"
        print(error_message, file=sys.stderr)
        return False
