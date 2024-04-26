#!/usr/bin/python3
"""takes letter and sends POST request to url with letter as par"""
import requests
import sys


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}
    response = requests.post(url, data=data)
    try:
        json_resp = response.json()
        if json_resp:
            id_ = json_resp.get("id")
            name = json_resp.get("name")
            print(f"[{id_}] {name}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
