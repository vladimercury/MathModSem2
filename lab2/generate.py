import numpy as np
from sympy import diff
from math import *
x = 0
u = 2 * tan(1/2) * sin(x) + 2 * cos(x) + x ** 2 - 2
print(diff(u, x))