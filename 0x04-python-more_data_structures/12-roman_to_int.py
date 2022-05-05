#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or (roman_string is None):
        return (0)

    res = 0
    value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for i in range(0, len(roman_string)):
        if i == len(roman_string) - 1:
            res += value[roman_string[i]]
        elif value[roman_string[i]] >= value[roman_string[i + 1]]:
            res += value[roman_string[i]]
        else:
            res -= value[roman_string[i]]
    return res
