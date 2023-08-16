#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    m_copy = matrix.copy()
    for row in range(len(matrix)):
        m_copy[row] = list(map(lambda x: x**2, matrix[row]))
    return m_copy
