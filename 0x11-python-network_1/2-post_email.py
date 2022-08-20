#!/usr/bin/python3
'''script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)'''
import urllib.request
import sys
import urllib.parse


if __name__ == '__main__':
    dict_values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(dict_values)
    data = data.encode('utf-8')
    request = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as resp:
        print(resp.read().decode('utf-8')
