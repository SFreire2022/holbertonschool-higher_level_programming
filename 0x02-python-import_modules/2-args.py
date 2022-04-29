#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    ac = len(argv)
    if ac == 1:
        print("0 arguments.")
    elif ac == 2:
        print("1 argument:")
        print(f"{1}: {argv[1]}")
    else:
        print(f"{ac - 1} arguments:")
        for i in range(1, ac):
            print(f"{i}: {argv[i]}")
