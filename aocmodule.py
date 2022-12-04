"""
Advent of Code 2022 - Utilities Module
https://adventofcode.com/2022/
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


def sumiter(*iterables):
    return (sum(x) for x in zip(*iterables))
