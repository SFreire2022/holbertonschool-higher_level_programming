#!/usr/bin/python3
'''Script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id'''
import requests
import sys


if __name__ == '__main__':
    url = 'https://api.github.com/user'
    user = sys.argv[1]
    pwd = sys.argv[2]
    r = requests.get(url, auth=requests.auth.HTTPBasicAuth(user, pwd))
    print(r.json().get('id'))
