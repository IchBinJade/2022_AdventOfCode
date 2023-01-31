"""
Author: IchBinJade
Date: 2023-01-31

Advent of Code 2022 - Day 3 Solution Test
https://adventofcode.com/2022/day/3
"""

import unittest
from day_03 import part_one

class TestDay03(unittest.TestCase):

    def test_part_one(self):
        input = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg", "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]
        actual = part_one(input)
        expected = 157
        self.assertEqual(actual, expected, "Should return 157")


if __name__ == "__main__":
    unittest.main(exit=False)
