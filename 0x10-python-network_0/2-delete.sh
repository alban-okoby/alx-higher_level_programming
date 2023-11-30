#!/bin/bash
# delete request to the URL passet as the first arg

url="$1"

if [ -z "$url" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

response=$(curl -sL -X DELETE "$url")
echo "$response \"I'm a DELETE request\""
