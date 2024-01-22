#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as e:
        error_msg = f"Exception: {e}"
        print(error_msg, file=sys.stderr)
        return None
