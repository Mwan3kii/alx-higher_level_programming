#!/bin/bash
# Sends DELETE request to URL passed as first argument displays body of response
curl -s -X DELETE "$1"
