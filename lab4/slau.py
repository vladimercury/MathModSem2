import numpy as np
a = np.asarray([[3, 5, 1], [3, 6, 8], [4, 1, 12]])
b = np.asarray([4, 7, 1])
print(np.linalg.solve(a, b))
print(np.linalg.solve(-a, b))
print(np.linalg.solve(-a, -b))