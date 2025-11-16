"""
Advent of Code 2022 - Utilities Module
https://adventofcode.com/2022/
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from operator import add, sub
from itertools import tee


def sliding_window(iterable, n):
    """
    Creates a sliding window of size n over an iterable object
    Returns a generator of n-tuples
    """
    iterators = tee(iterable, n)
    for i, iterator in enumerate(iterators):
        for _ in range(i):
            next(iterator, None)
    return zip(*iterators)


def sumiter(*iterables):
    return (sum(x) for x in zip(*iterables))


class Vector(tuple):
    """
    Simple 1-dimensional numeric array
    """
    
    @property
    def dimension(self):
        return len(self)
    
    def __add__(self, b):
        return Vector(map(add, self, b))
    
    def __sub__(self, b):
        return Vector(map(sub, self, b))
    
    def __mul__(self, k):
        return Vector(x*k for x in self)
    
    def __rmul__(self, k):
        return Vector(x*k for x in self)
    
    def __truediv__(self, k):
        return Vector(x/k for x in self)
    
    def __floordiv__(self, k):
        return Vector(x//k for x in self)
    
    def __index__(self, ix):
        return self[ix]
    
    def elementwise(self, function):
        return Vector(map(function, self))
