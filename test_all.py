#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2022 - Tests

Simple test script, nothing fancy
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from importlib import import_module
import unittest


class TestResults(unittest.TestCase):

    solutions = {'day01': [69883, 207576],
                 'day02': [11475, 16862],
                 'day03': [7826, 2577],
                 'day04': [494, 833],
                 'day05': ['FJSRQCFTN', 'CJVLJQPHS'],
                 'day06': [1757, 2950],
                 'day07': [1428881, 10475598],
                 'day08': [1829, 291840],
                 'day09': [6332, 2511]}

    def test_results(self):
        """
        Test all challenges scripts results
        """
        for script in self.solutions:
            print("\nTesting {0}.py...".format(script))
            with self.subTest(i=script):
                module = import_module(script)
                self.assertEqual(module.main(), self.solutions[script])
        print("\nAll done")


if __name__ == '__main__':
    unittest.main()
