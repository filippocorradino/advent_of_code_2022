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


class Vector(object):
    """
    Simple 1-dimensional numeric array

    TODO: evaluate if this can directly be a subclass of tuple
    """

    def __init__(self, coordinates:tuple):
        self.coordinates = coordinates
    
    @property
    def dimension(self):
        return len(self.coordinates)
    
    def __add__(self, b):
        return Vector(tuple(map(add, self.coordinates, b.coordinates)))
    
    def __sub__(self, b):
        return Vector(tuple(map(sub, self.coordinates, b.coordinates)))
    
    def __mul__(self, k):
        return Vector(tuple(x*k for x in self.coordinates))
    
    def __rmul__(self, k):
        return Vector(tuple(x*k for x in self.coordinates))
    
    def __truediv__(self, k):
        return Vector(tuple(x/k for x in self.coordinates))
    
    def __floordiv__(self, k):
        return Vector(tuple(x//k for x in self.coordinates))
    
    def __index__(self, ix):
        return self.coordinates[ix]
    
    def __iter__(self):
        return self.coordinates.__iter__()
    
    def __repr__(self) -> str:
        return f"{self.coordinates}"
    
    def elementwise(self, function):
        return Vector(tuple(map(function, self.coordinates)))
