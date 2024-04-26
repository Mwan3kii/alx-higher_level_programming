#!/usr/bin/python3
import urllib.request
import sys
url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    headers = response.headers
    x_request_var = headers.get("X-Request-Id")
    print(x_request_var)
