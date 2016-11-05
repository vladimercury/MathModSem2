import numpy
import conjugate_gradient.cg_util as cgutil
from util.checkdim import check_dimensions


def solve(a, b, eps=0.001):
    a, b = numpy.asarray(a), numpy.asarray(b)
    check_dimensions(a, b)
    x = numpy.zeros(b.shape)
    r = cgutil.compute_r(a, x, b)
    r_stat = [numpy.linalg.norm(r)]
    x_stat = [x]
    p = r.copy()
    while True:
        alpha = numpy.dot(r, r) / numpy.dot(numpy.dot(p, a), p)
        x = x + alpha * p
        x_stat.append(x)
        r_prev = r
        r = r - alpha * numpy.dot(a, p)
        r_stat.append(numpy.linalg.norm(r))
        if r_stat[-1] < eps:
            break
        beta = numpy.dot(r, r) / numpy.dot(r_prev, r_prev)
        p = r + beta * p
    return x, r_stat, x_stat
