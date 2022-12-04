#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2022 - Day 03
https://adventofcode.com/2022/day/03

Solution 1: 7826
Solution 2: 2577
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from functools import reduce
from itertools import islice


def priority(char):
    if not char.isalpha():
        raise ValueError
    if char.islower():
        return ord(char) - 96  # a-z = 1-26
    else:
        return ord(char) - 38  # A-Z = 27-52


def main(ifile='inputs/day_03_input.txt'):
    errors, badges = [], []
    with open(ifile) as file:
        while team := list(islice(file, 3)):
            rucksacks = [line.strip() for line in team]
            for rucksack in rucksacks:
                half = len(rucksack) // 2
                both = set(rucksack[:half]).intersection(set(rucksack[half:]))
                errors.append(both.pop())
            badge = reduce(lambda x, y: x.intersection(y),
                           (set(k) for k in rucksacks))
            badges.append(badge.pop())
    result = [sum(map(priority, x)) for x in (errors, badges)]
    print(f"The sum of the wrong items priorities is {result[0]}")
    print(f"The sum of the badges priorities is {result[1]}")
    return result
    

if __name__ == "__main__":
    main()
