#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2022 - Day 09
https://adventofcode.com/2022/day/09

Solution 1: 6332
Solution 2: 2511

TODO: make a bit more efficient?
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from collections import namedtuple
from aocmodule import Vector


Move = namedtuple('Move', ['direction', 'steps'])


MOVES_DICT = {'U': Vector((0, +1)),
              'D': Vector((0, -1)),
              'L': Vector((-1, 0)),
              'R': Vector((+1, 0))}


def node_motion(ante:Vector, post:Vector):
    diff = post - ante
    # post only moves if ante-post distance on any dimension is > 1
    if any(diff.elementwise(lambda x: abs(x) > 1)):
        # post "sticks" to the nearest of ante's four closest neighbours (UDLR)
        post = ante + (diff/2).elementwise(round)  # Magic!
    return post


def simulate_rope(ifile, knots, start=(0, 0)):
    nodes = [Vector(start) for _ in range(knots)]
    with open(ifile) as file:
        lines = (line.split() for line in file)
        moves = (Move(d, int(s)) for d, s in lines)
        for move in moves:
            for _ in range(move.steps):
                nodes[0] += MOVES_DICT[move.direction]
                for i in range(1, knots):
                    nodes[i] = node_motion(nodes[i-1], nodes[i])
                yield nodes


def main(ifile='inputs/day_09_input.txt', knots=[2, 10]):
    results = []
    for k in knots:
        result = len(set(nodes[-1] for nodes in simulate_rope(ifile, k)))
        results.append(result)
        print(f"The number of positions visited by the tail with a rope of "
              f"{k} knots is {result}")
    return results
    

if __name__ == "__main__":
    main()
