import numpy as np
import pylab as pt

n = 1000
# g = np.asarray([(t+1)/n for t in range(n)])
t = np.arange(0, n+1)
g = np.linspace(0, 1, n+1)
h, hg = np.zeros(n+1), np.zeros(n+1)
for i in reversed(t[1:-1]):
    hg[i] = hg[i+1] + 1 / i
    h[i] = g[i] * hg[i]
pt.plot(t, g)
pt.plot(t, h)
pt.show()