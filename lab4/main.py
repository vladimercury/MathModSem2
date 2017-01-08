import conjugate_gradient.conjugate_gradient_solver as cgs
from lab4.datagen import generate
import util.stat as stat

import numpy as np
import numpy.linalg as la

from math import log, sqrt
import pylab as pt

a, x, b = generate(50)
z = la.eig(a)[0]
print(sorted(z))

#  SOLUTION
x_res, r, x_stat = cgs.solve(a, b, eps=0.01)
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

