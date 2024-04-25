#!/usr/bin/python3
def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    low = 0
    high = len(list_of_integers) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and\
           (mid == high or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]
        if mid < high and list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid - 1
    return None
