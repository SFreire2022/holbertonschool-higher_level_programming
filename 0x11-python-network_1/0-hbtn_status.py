#!/usr/bin/python3
'''Request URL and open to a file using with, print content of response
using required format'''
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as resp:
        cont = resp.read()
        print('Body response:')
        print('\t- type: {}'.format(type(cont)))
        print('\t- content: {}'.format(cont))
        print('\t- utf8 content: {}'.format(cont.decode('utf-8')))
