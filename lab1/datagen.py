def generate(n=3):
    from random import random
    from numpy import asarray, dot
    a = [[random() for j in range(n)] for i in range(n)]
    for i in range(n):
        a[i][i] += sum(a[i])
    x = [random() for i in range(n)]
    a, x = asarray(a), asarray(x)
    return a, x, dot(a, x)
