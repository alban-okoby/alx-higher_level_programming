#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

response=$(curl -s -w "%{http_code}" "$1")
http_status=$(tail -c 3 <<< "$response")

if [ "$http_status" == "200" ]; then
    # Display the body
    body=$(head -c -3 <<< "$response")
    echo "Response Body:"
    echo "$body"
else
    echo "HTTP status code: $http_status"
fi
