#!/usr/bin/python3
for d in range(0, 8):
    for u in range(d + 1, 10):
        print(f"{d}{u}, ", end="")
print(f"{d + 1}{u}")
