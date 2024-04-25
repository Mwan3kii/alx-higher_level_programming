#!/usr/bin/python3
"""finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None
    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)
    mid = size // 2
    peak = list_of_integers[mid]
    if (mid == 0 or peak >= list_of_integers[mid - 1]) and \
       (mid == size - 1 or peak >= list_of_integers[mid + 1]):
        return peak
    if mid > 0 and list_of_integers[mid - 1] > peak:
        return find_peak(list_of_integers[:mid])
    return find_peak(list_of_integers[mid + 1:])
