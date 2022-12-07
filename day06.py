#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2022 - Day 06
https://adventofcode.com/2022/day/06

Solution 1: 1757
Solution 2: 2950
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from aocmodule import sliding_window


def find_marker(ifile, marker_length):
    with open(ifile) as file:
        buffer = sliding_window(*file, marker_length)
        for i, x in enumerate(buffer):
            if len(set(x)) == marker_length:
                break
    result = i + marker_length
    print(f"The first marker of length {marker_length} is found after "
          f"receiving {result} characters")
    return result


def main(ifile='inputs/day_06_input.txt', marker_lengths=[4, 14]):
    return [find_marker(ifile, n) for n in marker_lengths]
    

if __name__ == "__main__":
    main()
