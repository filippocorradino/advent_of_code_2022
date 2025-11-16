#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2022 - Day 11
https://adventofcode.com/2022/day/11

Solution 1: 55216
Solution 2: 12848882750
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from dataclasses import dataclass
from functools import reduce
from math import gcd
from typing import Callable, Dict, List


def lcm(a, b):
  return a*b // gcd(a, b)


@dataclass
class Monkey():
    items: List[int]
    operation: Callable[[int], int]
    divisor: int
    destination: Dict[bool, int]
    inspections: int = 0


class MonkeyTroop():

    def __init__(self, monkeys: dict, worry_drop: int):
        self.monkeys = monkeys
        self.turns = sorted(monkeys.keys())
        self.lcm = reduce(lcm, (m.divisor for m in self.monkeys.values()))
        self.worry_drop = worry_drop

    @classmethod
    def from_file(cls, ifile, worry_drop: int):
        monkeys = {}
        with open(ifile) as file:
            while True:
                try:
                    line = next(file)
                    if line.startswith('Monkey'):
                        id = int(line.split()[-1][:-1])
                        items = (next(file).split(':')[-1])
                        items = [int(x) for x in items.split(',')]
                        operation_string = next(file).split('=')[-1][1:-1]
                        def fun_constructor(string):
                            return lambda old: eval(string)
                        operation = fun_constructor(operation_string)
                        divisor = int(next(file).split()[-1])
                        destination = {False: int(next(file).split()[-1]),
                                       True:  int(next(file).split()[-1])}
                        monkeys[id] = Monkey(items=items,
                                             operation=operation,
                                             divisor=divisor,
                                             destination=destination)
                except StopIteration:
                    break
        return cls(monkeys, worry_drop)
    
    def round(self):
        for id in self.turns:
            monkey: Monkey = self.monkeys[id]
            for item in monkey.items:
                worry = (monkey.operation(item) // self.worry_drop) % self.lcm
                destination = monkey.destination[bool(worry % monkey.divisor)]
                self.monkeys[destination].items.append(worry)
            monkey.inspections += len(monkey.items)
            monkey.items = []


def main(ifile='inputs/day_11_input.txt', rounds=[20, 10000], worry_drop=[3, 1]):
    results = []
    for r, wd in zip(rounds, worry_drop):
        troop = MonkeyTroop.from_file(ifile, worry_drop=wd)
        for _ in range(r):
            troop.round()
        inspections = sorted([m.inspections for m in troop.monkeys.values()])
        monkey_business = inspections[-1] * inspections[-2]
        results.append(monkey_business)
        print(f"The level of monkey business after {r} rounds is {monkey_business}")
    return results

if __name__ == "__main__":
    main()
