import numpy as np
import math
import numpy.linalg as la
import pylab as pt


def generate_matrix(n, delta):
    matrix = np.zeros((n - 1, n - 1))
    delta_2 = 1 / (delta ** 2)
    for i in range(n - 1):
        matrix[i][i] = -2 * delta_2 + 1
    for i in range(1, n - 1):
        matrix[i][i-1], matrix[i-1][i] = delta_2, delta_2
    return matrix

A = generate_matrix(5, 1/5)
print(la.inv(A))