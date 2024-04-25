#!/usr/bin/python3
def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    def help_peak(low, high):
        if high - low == 1:
            return list_of_integers[low]
        mid = low + (high - low) // 2
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
           (mid == high - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            return help_peak(mid + 1, high)
        return help_peak(low, mid)
    return help_peak(0, len(list_of_integers))
