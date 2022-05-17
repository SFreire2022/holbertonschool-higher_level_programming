#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if not my_list or x == 0:
        print()
        return (0)
    num = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num = num + 1
        except (ValueError, TypeError, IndexError):
            pass
    print()
    return(num)
