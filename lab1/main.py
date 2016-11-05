import jacobi.jacobi_lin_solver as jls
import jacobi.jacobi_stat as jstat
import pylab as pt
from math import log
from lab1.datagen import generate

a, x, b = generate()

#  SOLUTION
x_res, r, x_stat = jls.solve(a, b, eps=0.01)
rl = [log(i) for i in r]
diff = jstat.diff(x, x_stat)
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
