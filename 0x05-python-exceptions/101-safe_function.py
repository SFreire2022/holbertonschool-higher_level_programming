#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        res = fct(*args)
    except Exception as error:
        print("Exception:", error, file=sys.stderr)
        res = None
    finally:
        return (res)
