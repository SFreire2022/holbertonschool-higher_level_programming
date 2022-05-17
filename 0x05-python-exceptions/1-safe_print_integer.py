def safe_print_integer(value):
    try:
        print(f'{value[:d]}')
        return (True)
    except AttributeError:
        return (False)
