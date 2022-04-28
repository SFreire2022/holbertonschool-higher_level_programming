#!/usr/bin/python3
# Import function add from file add_0.
# if stand alone executed print the resoult with default values.
from add_0 import add
if __name__ == "__main__":
    a = 1
    b = 2
    print(f"{a} + {b} = {add(a, b)}")
