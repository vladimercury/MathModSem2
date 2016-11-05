import numpy
import jacobi.jacobi_util as jutil


def solve(a, b, eps=0.001):
    a, b = numpy.asarray(a), numpy.asarray(b)
    jutil.check_dimensions(a, b)
    a1, d, a2 = jutil.split_matrix(a)
    if jutil.convergence(a, d) >= 1:
        raise numpy.linalg.LinAlgError("Convergence condition fails")
    x = numpy.zeros(b.shape)
    r = jutil.compute_r(b, a, x)
    r_stat = [numpy.linalg.norm(r)]
    x_stat = [x]
    while r_stat[-1] >= eps:
        z = jutil.compute_z(d, r)
        x = jutil.compute_x(x, z)
        r = jutil.compute_r(b, a, x)
        r_stat.append(numpy.linalg.norm(r))
        x_stat.append(x)
    return x, r_stat, x_stat