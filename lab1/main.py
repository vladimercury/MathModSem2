from math import log

import pylab as pt

import jacobi.jacobi_lin_solver as jls
import util.stat as stat
from lab1.datagen import generate

a, x, b = generate()

#  SOLUTION
x_res, r, x_stat = jls.solve(a, b)
rl = [log(i) for i in r]
diff = stat.diff(x, x_stat)
diffl = [log(i) for i in diff]


#  VISUALIZATION
pt.plot(range(len(r)), r)
pt.title("r graph")
pt.xlabel("iteration")
pt.ylabel("r")
pt.figure()

pt.title("Log(r) graph")
pt.xlabel("iteration")
pt.ylabel("log(r)")
pt.plot(range(len(rl)), rl, color='red')
pt.figure()

pt.plot(range(len(diff)), diff)
pt.title("pogr graph")
pt.xlabel("iteration")
pt.ylabel("pogr")
pt.figure()

pt.plot(range(len(diffl)), diffl, color='red')
pt.title("log(pogr) graph")
pt.xlabel("iteration")
pt.ylabel("pogr")
pt.show()
