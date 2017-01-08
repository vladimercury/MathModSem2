from math import log

import pylab as pt
import numpy

import jacobi.jacobi_lin_solver as jls
import util.stat as stat
from lab1.datagen import generate

#  SOLUTION
a, x, b = [], [], []
# while True:
#     try:
#         a, x, b = generate()
#         jls.solve(a, b)
#     except numpy.linalg.LinAlgError:
#         continue
#     break

a = numpy.asarray([[3, 1, 1], [1, 3, 1], [1, 1, 3]])
x = numpy.asarray([1, 1, 1])
b = numpy.dot(a, x)

a2 = a * 2
x2 = x
b2 = numpy.dot(a2, x)
data = [(a, b, x), (a2, b2, x2)]
j = 0
for i in data:
    x_res, r, x_stat = jls.solve(i[0], i[1])
    r = [10e-7 if x == 0 else x for x in r]
    rl = [log(i) for i in r]
    diff = stat.diff(i[2], x_stat)
    diff = [10e-7 if x == 0 else x for x in diff]
    diffl = [log(i) for i in diff]

    print(x_res)
    print(r)
    print(diff)
    print(diffl)
    print(len(r) - 1)


    #  VISUALIZATION
    # pt.plot(range(len(r)), r)
    # pt.title("r graph")
    # pt.xlabel("iteration")
    # pt.ylabel("r")
    # pt.figure()
    #
    pt.title("Log(r) graph")
    pt.xlabel("iteration")
    pt.ylabel("log(r)")
    pt.plot(range(len(rl)), rl, color='red')
    pt.figure()
    #
    # pt.plot(range(len(diff)), diff)
    # pt.title("pogr graph")
    # pt.xlabel("iteration")
    # pt.ylabel("pogr")
    # pt.figure()

    def approx(arr):
        n = len(arr)
        sumx = sum(range(n))
        sumy = sum(arr)
        sumx2 = sum([x*x for x in range(n)])
        sumxy = sum([x*arr[x] for x in range(n)])
        a = (n * sumxy - sumx * sumy) / (n * sumx2 - sumx * sumx)
        b = (sumy - a * sumx) / n
        return a, b

    xx = 0

    print(log(diff[-1])/(diffl[1]))
    a, b = approx(diffl[:3])
    app2 = [a*x + b for x in range(len(diffl) + xx)]
    print((log(diff[-1]) - b)/(a))
    a, b = approx(diffl[:4])
    app3 = [a*x + b for x in range(len(diffl) + xx)]
    print((log(diff[-1]) - b)/(a))

    pt.plot(range(len(diffl)), diffl, color='blue')
    pt.plot(range(len(diffl) + xx), [x * diffl[1] for x in range(len(diffl) + xx)], color='red', linestyle='dashed')
    pt.plot(range(len(diffl) + xx), app2, color='orange', linestyle='dashed')
    pt.plot(range(len(diffl) + xx), app3, color='green', linestyle='dashed')
    pt.plot(range(len(diffl) + xx), [diffl[-1] for x in range(len(diffl) + xx)], color='black', linestyle='dotted')
    pt.title("log(pogr) graph")
    pt.xlabel("iteration")
    pt.ylabel("pogr")
    if j == 0:
        pt.figure()
    j += 1
pt.show()

