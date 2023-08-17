#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (ist(map(lambda value: list(map(lambda v2: v2**2, value)), matrix))
