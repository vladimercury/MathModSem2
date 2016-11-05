def check_dimensions(a, b):
    x, y = a.shape, b.shape
    if not x or not y:
        raise ValueError('Empty dimension')
    if x[0] != x[1]:
        raise ValueError('A is not a square matrix')
    if y[0] != x[0]:
        raise ValueError('Different dimensions')

