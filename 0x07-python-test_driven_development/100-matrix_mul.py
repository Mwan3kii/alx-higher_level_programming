#!/usr/bin/python3
"""This function multiplies 2 matrices."""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices.

    Args:
    m_a (list of lists): First matrix.
    m_b (list of lists): Second matrix.

    Returns:
    list of lists: Resulting matrix.

    Raises:
        TypeError: If m_a or m_b is not a list or not interger.
        ValueError: If m_a or m_b is empty or can't be multiplied.
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list" if not isinstance(m_a, list) else "m_b must be a list")
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists" if not all(isinstance(row, list) for row in m_a)
                else "m_b must be a list of lists")
    if not m_a or not all(row for row in m_a) or not m_b or not all(row for row in m_b):
        raise ValueError("m_a can't be empty" if not m_a or not all(row for row in m_a) else "m_b can't be empty")
    if not all(isinstance(element, (int, float)) for row in m_a for element in row) or \
            not all(isinstance(element, (int, float)) for row in m_b for element in row):
        raise TypeError("m_a should contain only integers or floats" if not all(isinstance(element, (int, float)) for row in m_a for element in row)
                else "m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size" if not all(len(row) == len(m_a[0]) for row in m_a)
                else "each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]
    return result
