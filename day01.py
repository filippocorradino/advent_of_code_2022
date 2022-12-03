#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2022 - Day 01
https://adventofcode.com/2022/day/01

Solution 1: 69883
Solution 2: 207576
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


def calories_counter(ifile, n=1):
    max_elves_calories = [0,] * n
    current_elf_calories = 0
    with open(ifile) as file:
        for calories in (line.strip() for line in file):
            if calories:
                current_elf_calories += int(calories)
            else:
                max_elves_calories.append(current_elf_calories)
                max_elves_calories.sort()
                max_elves_calories = max_elves_calories[1:]
                current_elf_calories = 0
    result = sum(max_elves_calories)
    print(f"The top {n} elves bring a total of {result} calories")
    return result


def main(ifile='inputs/day_01_input.txt', elves=[1, 3]):
    return [calories_counter(ifile, n) for n in elves]
    

if __name__ == "__main__":
    main()
