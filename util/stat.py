from numpy import asarray
from numpy.linalg import norm
from math import fabs


def diff(x, x_stat):
    x_norm = norm(x)
    return [norm(asarray([fabs(i) for i in y - x])) / x_norm for y in x_stat]