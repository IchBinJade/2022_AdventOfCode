"""
Author: IchBinJade
Date: 2022-12-16

Advent of Code 2022 - Day 2 Solution
https://adventofcode.com/2022/day/2
"""

import unittest
from day_02 import part_one, part_two

class TestDay02(unittest.TestCase):

    def test_part_one(self):
        input = ["A Y", "B X", "C Z"]
        actual = part_one(input)
        expected = 15
        self.assertEqual(actual, expected, "Should return 15")

    def test_part_two(self):
        input = ["A Y", "B X", "C Z"]
        actual = part_two(input)
        expected = 12
        self.assertEqual(actual, expected, "Should return 12")
        return None


if __name__ == "__main__":
    unittest.main(exit=False)
