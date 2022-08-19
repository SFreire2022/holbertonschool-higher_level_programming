#!/bin/bash
#Script that takes in a URL and displays all HTTP methods the server will accept.
curl -siLX "OPTIONS" "$1" | grep "Allow" | awk 'BEGIN {FS = ": "} {print $2}'
