#!/bin/bash
# Takes URL sends GET request to URL and displays the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
