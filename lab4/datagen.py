import numpy
import random


def generate(n=3):
    a = generate_a(n)
    x = numpy.asarray([random.random() * n for i in range(n)])
    return a, x, numpy.dot(a, x)

def generate_a(n=3):
    return numpy.ones((n, n)) + numpy.diag(range(n, n+n))

def generate_a_rand(n=3):
    a = numpy.zeros((n, n))
    for i in range(n):
        for j in range(n):
            a[i][j] = random.random()
    return numpy.dot(a, a.transpose())
