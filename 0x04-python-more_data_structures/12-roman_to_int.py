#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numbers = [roman_dict[n] for n in roman_string] + [0]
    total = 0
    for x in range(len(numbers) - 1):
        if numbers[x] >= numbers[x + 1]:
            total += numbers[x]
        else:
            total += numbers[x]
    return total
