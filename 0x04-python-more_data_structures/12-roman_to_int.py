#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    roman_dict = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
            }
    total = 0
    prev_value = 0

    for x in roman_string[::-1]:
        curr = roman_dict[x]
        if curr >= prev_value:
            total += curr
        else:
            total -= curr
        prev_value = curr
    return total
