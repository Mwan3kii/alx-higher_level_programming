#!/usr/bin/python3
"""Takes URL sends request displays X-Request-Id in response header"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    x_request_var = response.headers.get("X-Request-Id")
    print(x_request_var)
