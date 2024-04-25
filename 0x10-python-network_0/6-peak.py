#!/usr/bin/python3
def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    def help_peak(low, high):
        mid = (low + high) // 2
        if (
            (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1])
            and (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1])
        ):
            return list_of_integers[mid]
        if mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            return help_peak(low, mid - 1)
        return help_peak(mid + 1, high)
    return help_peak(0, len(list_of_integers) - 1)
