#!/bin/bash
# Requests 0.0.0.0:5000/catch_me that causes server to respond with a message
curl -sL -X PUT -d "user_id=98" -H "Origin: School" 0.0.0.0:5000/catch_me
