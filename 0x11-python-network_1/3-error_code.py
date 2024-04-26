#!/usr/bin/python3
"""Takes URL sends a request to URL and displays the body of response"""
import urllib.error
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body_resp = response.read().decode("utf-8")
            print(body_resp)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
