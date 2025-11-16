#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2022 - Day 10
https://adventofcode.com/2022/day/10

Solution 1: 14780
Solution 2: ELPLZGLZ
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


def register_sequence(ifile):
    # Returns values of the register DURING cycle X
    register = 1
    yield register  # Register during cycle 1
    with open(ifile) as file:
        for line in file:
            yield register  # Both for noop and addx
            if line.startswith('addx'):
                register += int(line.split()[-1])
                yield register


def main(ifile='inputs/day_10_input.txt'):
    strenght = 0
    screen = ''
    for cycle, register in enumerate(register_sequence(ifile), start=1):
        if not((cycle-20) % 40):
            strenght += cycle * register
        pixel = cycle % 40 - 1
        if abs(register - pixel) <= 1:
            screen += '#'
        else:
            screen += '.'
        if not(cycle % 40):
            screen += '\n'
    screen = screen[:-2]  # Drop final newline + pixel belonging to next refresh
    print(f"The signal strength is {strenght}")
    print(f"The screen prints:\n{screen}")
    return [strenght, screen]
    

if __name__ == "__main__":
    main()
