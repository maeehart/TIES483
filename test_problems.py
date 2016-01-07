def rosenbrock(x):
    """
    This R^2 -> R^1 function should be compatible with algopy.
    http://en.wikipedia.org/wiki/Rosenbrock_function
    A generalized implementation is available
    as the scipy.optimize.rosen function
    """
    a = 1. - x[0]
    b = x[1] - a*a
    return a*a + b*b*100.