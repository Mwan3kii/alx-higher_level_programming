#!/usr/bin/python3
"""Takes URL, email sends POST request URL email displays body of response"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("utf-8")
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        resp_con = response.read().decode("utf-8")
        print(resp_con)
