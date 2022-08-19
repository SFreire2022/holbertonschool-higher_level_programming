#!/bin/bash
#Shell script thath return de content-length of the http response
curl -sI $1 | grep "Content-Length" | awk '{print $2}'
