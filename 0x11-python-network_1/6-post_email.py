#!/usr/bin/python3
"""Takes url and email sends POST request and displays body response"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {"email": email}
    response = requests.post(url, data=data)
    body_resp = response.text
    print(body_resp)
