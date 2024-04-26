#!/usr/bin/python3
"""Takes repo name and owner name and displays the commits"""
import sys
import requests


def get_commits(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)
    commits = response.json()
    return commits


def print_commits(commits):
    for com in commits[:10]:
        sha = com['sha']
        author_name = com['commit']['author']['name']
        print(f"{sha}: {author_name}")


if __name__ == "__main__":
    owner = sys.argv[2]
    repo = sys.argv[1]
    commits = get_commits(owner, repo)
    print_commits(commits)
