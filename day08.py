#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2022 - Day 08
https://adventofcode.com/2022/day/08

Solution 1: 1829
Solution 2: 291840

Waiver to O(1) memory because I'm not (yet) mad
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


def scan_tree_line(tree_line):
    max_tree = -1
    visible_ixs = []
    for ix, tree in enumerate(tree_line):
        if tree > max_tree:
            max_tree = tree
            visible_ixs.append(ix)
    return visible_ixs


def scenic_score(tree_map, ir, ic):
    score = 1
    nr = len(tree_map)
    nc = len(tree_map[0])
    tree = tree_map[ir][ic]
    # Scan up
    dc = 0
    for dc in range(1, ic+1):
        if tree_map[ir][ic-dc] >= tree:
            break
    score *= dc
    # Scan down
    dc = 0
    for dc in range(1, nc-ic):
        if tree_map[ir][ic+dc] >= tree:
            break
    score *= dc
    # Scan left
    dr = 0
    for dr in range(1, ir+1):
        if tree_map[ir-dr][ic] >= tree:
            break
    score *= dr
    # Scan right
    dr = 0
    for dr in range(1, nr-ir):
        if tree_map[ir+dr][ic] >= tree:
            break
    score *= dr
    return score


def main(ifile='inputs/day_08_input.txt'):
    with open(ifile) as file:
        tree_map = [[int(x) for x in line.strip()]
                     for line in file.readlines()]  # Sigh :(
    visible_trees = set()
    # Scan rows
    for ir, row in enumerate(tree_map):
        for ic in scan_tree_line(row):
            visible_trees.add((ir, ic))
        for ic in scan_tree_line(reversed(row)):
            visible_trees.add((ir, len(row)-ic-1))
    # Scan columns
    for ic, col in enumerate(zip(*tree_map)):
        for ir in scan_tree_line(col):
            visible_trees.add((ir, ic))
        for ir in scan_tree_line(reversed(col)):
            visible_trees.add((len(col)-ir-1, ic))
    num_visible_trees = len(visible_trees)
    print(f"There are {num_visible_trees} visible from the outside")
    # Scenic scores
    max_score = 0
    for ir, row in enumerate(tree_map):
        for ic, _ in enumerate(row):
            max_score = max(max_score, scenic_score(tree_map, ir, ic))
    print(f"The maximum scenic score is {max_score}")
    return [num_visible_trees, max_score]
    

if __name__ == "__main__":
    main()
