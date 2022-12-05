#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2022 - Day 05
https://adventofcode.com/2022/day/05

Solution 1: FJSRQCFTN
Solution 2: CJVLJQPHS
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


CRANE_MODEL_SPECS = {9000: True, 9001: False}


def crane_operation(filegen, crates_dict, crane):
    for instruction in filegen:
        n, src, dst = map(int, instruction.split()[1::2])
        moving_crates = crates_dict[src][-n:]
        crates_dict[src] = crates_dict[src][:-n]
        if CRANE_MODEL_SPECS[crane]:
            moving_crates = moving_crates[::-1]
        crates_dict[dst] += moving_crates
    return


def final_top_crates(ifile, crane):
    with open(ifile) as file:
        # Create a dict of all the crate piles, pile: (bot, ..., top)
        # Crates piles are saved as strings
        crates_levels = []
        while line := next(file).strip('\n'):
            crates_levels.append(line[1::4])  # Get crate letters and pile nums
        crates_levels.reverse()  # Order the levels bottom to top
        crates_list = [''.join(x) for x in zip(*crates_levels)]  # Rows to Cols
        crates_dict = {int(x[0]): x[1:].strip(' ') for x in crates_list}
        # Now follow the crane instructions and check the top crates
        crane_operation(file, crates_dict, crane)
        top_crates = ''.join(crates_dict[x][-1] for x in crates_dict)
        print(f"The top crates with the CrateMover {crane} are {top_crates}")
    return top_crates


def main(ifile='inputs/day_05_input.txt'):
    return [final_top_crates(ifile, crane) for crane in CRANE_MODEL_SPECS]
    

if __name__ == "__main__":
    main()
