#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2022 - Day 04
https://adventofcode.com/2022/day/04

Solution 1: 494
Solution 2: 833
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from aocmodule import sumiter


def any_overlap(pair):
    return ((pair[1][0] <= pair[0][1] <= pair[1][1]) or
            (pair[0][0] <= pair[1][1] <= pair[0][1]))


def full_overlap(pair):
    return ((pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]) or
            (pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][1]))


def main(ifile='inputs/day_04_input.txt'):
    with open(ifile) as file:
        # file line = a-b,c-d --> pair = [[a, b], [c, d]]
        pairs = ([[int(x) for x in task.split('-')]
                 for task in line.strip().split(',')]
                 for line in file)
        overlaps = ((int(full_overlap(x)), int(any_overlap(x))) for x in pairs)
        result = list(sumiter(*overlaps))  # "Column-wise" sum of overlaps
    print(f"There are {result[0]} full overlaps")
    print(f"There are {result[1]} partial overlaps")
    return result
    

if __name__ == "__main__":
    main()
