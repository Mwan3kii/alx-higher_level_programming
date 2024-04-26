#!/usr/bin/python3
import urllib.request
url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    content = response.read()
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}") 
    utf8_content = content.decode("utf-8", errors="replace")
    print(f"\t- utf8 content: {utf8_content}")
