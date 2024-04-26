#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
import requests
url = "https://alx-intranet.hbtn.io/status"
response = requests.get(url)
content = response.text
print("Body response:")
print(f"\t- type: {type(content)}")
print(f"\t- content: {content}")
