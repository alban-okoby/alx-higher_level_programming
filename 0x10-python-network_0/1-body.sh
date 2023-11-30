#!/bin/bash

url="$1"

# Check if URL is provided
if [ -z "$url" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

response=$(curl -sL -w "%{http_code}" "$url")
http_code=${response: -3}

if [ "$http_code" = "200" ]; then
    echo "${response::-3}"
else
    echo "Failed to retrieve response. HTTP status code: $http_code"
    exit 1
fi
