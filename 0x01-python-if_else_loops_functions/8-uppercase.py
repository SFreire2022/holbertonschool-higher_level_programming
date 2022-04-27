#!/usr/bin/python3
def uppercase(str):
    for c in range(len(str)):
        i = ord(str[c])
        if (i > 96 and i < 123):
            i -= 32
        print(f"{chr(i)}", end="")
    print()
