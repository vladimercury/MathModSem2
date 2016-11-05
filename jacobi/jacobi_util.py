import numpy


def check_dimensions(a, b):
    x, y = a.shape, b.shape
    if not x or not y:
        raise ValueError('Empty dimension')
    if x[0] != x[1]:
        raise ValueError('A is not a square matrix')
    if y[0] != x[0]:
        raise ValueError('Different dimensions')


def compute_r(b, a, x):
    return b - numpy.dot(a, x)


def compute_x(x, z):
    return x + z


def compute_z(d, r):
    return numpy.dot(numpy.linalg.inv(d), r)


def convergence(a, d):
    e = numpy.identity(a.shape[0])
    d1 = numpy.linalg.inv(d)
    return numpy.linalg.norm(e - numpy.dot(d1, a), 1)


def split_matrix(a):
    a1 = numpy.tril(a, -1)  # below diagonal
    d = numpy.diag(numpy.diag(a))  # diagonal
    a2 = numpy.triu(a, 1)  # above diagonal
    return a1, d, a2
