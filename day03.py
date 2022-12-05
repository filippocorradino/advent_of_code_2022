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
    errors, badges = 0, 0
    with open(ifile) as file:
        # Work by elf team (3 elves per team)
        while team := list(islice(file, 3)):
            rucksacks = [line.strip() for line in team]
            # Find misplaced items at elf level
            for rucksack in rucksacks:
                half = len(rucksack) // 2
                both = set(rucksack[:half]) & (set(rucksack[half:]))
                errors += priority(both.pop())  # Set to char
            # Find common badge item at team level
            badge = reduce(lambda x, y: x & y,
                           (set(k) for k in rucksacks))
            badges += priority(badge.pop())  # Set to char
    print(f"The sum of the wrong items priorities is {errors}")
    print(f"The sum of the badges priorities is {badges}")
    return [errors, badges]
    

if __name__ == "__main__":
    main()
