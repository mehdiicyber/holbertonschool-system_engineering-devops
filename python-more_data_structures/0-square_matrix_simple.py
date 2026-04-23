#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for x in matrix:
        a = []
        for i in x:
            i = i ** 2
            a.append(i)
        new_matrix.append(a)
    return new_matrix
    return matrix
