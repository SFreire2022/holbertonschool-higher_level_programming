#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys

    try:
        print("{:d}".format(value))
    except Exception as error:
        print("Exception:", error, file=sys.stderr)
        res = False
    else:
        res = True
    finally:
        return(res)
