#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    dir(hidden_4)
    for name in dir(hidden_4):
        if name[0:2] != "__":
            print(f"{name}")
