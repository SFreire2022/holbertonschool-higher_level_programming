#!/usr/bin/python3
"""Script that adds all arguments to a Python list object,
and save them to a JSON file"""
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    myfile = open(filename, 'r')
    myobj = load_from_json_file(filename)
except Exception:
    myobj = []

for arg in argv[1:]:
    myobj.append(arg)

save_to_json_file(myobj, "add_item.json")
