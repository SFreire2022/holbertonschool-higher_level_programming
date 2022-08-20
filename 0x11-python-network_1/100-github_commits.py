#!/usr/bin/python3
'''Script that takes 2 arguments in order to solve this challenge.
The first argument will be the repository name
The second argument will be the owner name'''
import requests
import sys


if __name__ == "__main__":
    try:
        repo = sys.argv[1]
        owner = sys.argv[2]
        url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
        r = requests.get(url)
        json = r.json()
        for i in range(0, 10):
            print('{}: {}'.format(json[i].get('sha'), json[i].get(
                  'commit').get('author').get('name')))
    except Exception:
        pass
