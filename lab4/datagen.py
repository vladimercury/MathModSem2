import numpy
import random


def generate(n=3):
    a = numpy.ones((n, n)) + numpy.diag(range(n, n+n))
    x = numpy.asarray([random.random() * n for i in range(n)])
    return a, x, numpy.dot(a, x)
