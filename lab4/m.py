from lab4.datagen import generate
import numpy.linalg as la
import numpy as np
import math
from pprint import pprint
A, x, b = generate(500)
k = np.dot(la.norm(A), la.norm(la.inv(A)))
k = (math.sqrt(k) - 1)/(math.sqrt(k) + 1)
a, it = 1, 0
while a > 0.01:
    a *= k
    it += 1
    print(a)
print(it)