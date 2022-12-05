#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2022 - Day 02
https://adventofcode.com/2022/day/02

Solution 1: 11475
Solution 2: 16862
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


# Only 9 cases in R-P-S, a LUT is cheap (wouldn't easily scale anyway!)
# A-B-C = X-Y-Z = R-P-S

POINTS_DICT_1 = {
    'A X': 4,  # 1 + 3 points
    'A Y': 8,  # 2 + 6 points
    'A Z': 3,  # 3 + 0 points
    'B X': 1,  # 1 + 0 points
    'B Y': 5,  # 2 + 3 points
    'B Z': 9,  # 3 + 6 points
    'C X': 7,  # 1 + 6 points
    'C Y': 2,  # 2 + 0 points
    'C Z': 6,  # 3 + 3 points
}
POINTS_DICT_2 = {
    'A X': 3,  # 3 + 0 points
    'A Y': 4,  # 1 + 3 points
    'A Z': 8,  # 2 + 6 points
    'B X': 1,  # 1 + 0 points
    'B Y': 5,  # 2 + 3 points
    'B Z': 9,  # 3 + 6 points
    'C X': 2,  # 2 + 0 points
    'C Y': 6,  # 3 + 3 points
    'C Z': 7,  # 1 + 6 points
}


def main(ifile='inputs/day_02_input.txt', elves=[1, 3]):

    def play(points_dict):
        with open(ifile) as file:
            score = sum(points_dict[line.strip()] for line in file)
            print(f"The total score is {score}")
        return score

    return [play(d) for d in (POINTS_DICT_1, POINTS_DICT_2)]
    

if __name__ == "__main__":
    main()
