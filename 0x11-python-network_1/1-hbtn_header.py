#!/usr/bin/python3
"""Displays value of X-Request-Id variable found in header of the response"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.headers
        x_request_var = headers.get("X-Request-Id")
        print(x_request_var)
