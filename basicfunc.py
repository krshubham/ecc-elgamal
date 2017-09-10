import collections
import os,sys

def inv(n, q):
    for i in range(q):
        if (n * i) % q == 1:
            return i
        pass
    assert False, "unreached"
    pass

def sqrt(n, q):
    assert n < q
    for i in range(1, q):
        if i * i % q == n:
            return (i, q - i)
        pass
    return (False, False)


Coord = collections.namedtuple("Coord", ["x", "y"])




