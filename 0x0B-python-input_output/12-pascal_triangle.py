#!/usr/bin/python3
"""This does pascal triangle."""


def pascal_triangle(n):
    """This returns lists of integers representing the Pascal’s triangle.

    Args:
        n: The n number.

    Returns:
        list a integers.
    """
    if n <= 0:
        return []
    result = []
    for k in range(n):
        row = [1] * (k + 1)
        for j in range(1, k):
            row[j] = result[k - 1][j - 1] + result[k - 1][j]
        result.append(row)
    return result
