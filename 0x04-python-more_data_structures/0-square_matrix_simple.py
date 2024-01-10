#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_list = []
    for row in matrix:
            squared_list.append([elem ** 2 for elem in row])
    return squared_list
