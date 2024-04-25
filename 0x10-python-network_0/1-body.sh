#!/bin/bash
# Bash script sends a GET request to URL and displays the body of the response
curl -s -w "\n%{http_code}" "$1" | awk 'NR==1 { body=$0; } NR==2 && $0 == "200" { print body; }'
