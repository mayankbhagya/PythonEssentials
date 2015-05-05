#currying: process of decomposing funcs into single arg funcs


def f(x, y, z):
    return x + 2*y + z


import functools
g = functools.partial(f, 3, 4)
# print g(4)
# print g(5)

#keyword args?