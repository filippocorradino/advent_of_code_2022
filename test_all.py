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

    solutions = {}

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
