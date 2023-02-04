"""
Author: IchBinJade
Date: 2023-02-04

Advent of Code 2022 - Day 4 Solution Test
https://adventofcode.com/2022/day/4
"""

import unittest
from day_04 import part_one

class TestDay04(unittest.TestCase):

    def test_part_one(self):
        input = ["2-4,6-8","2-3,4-5","5-7,7-9","2-8,3-7","6-6,4-6","2-6,4-8"]
        actual = part_one(input)
        expected = 2
        self.assertEqual(actual, expected, "Should return 2")
        
    #def test_part_two(self):
     #   input = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg", "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]
      #  actual = part_two(input)
       # expected = 70
        #self.assertEqual(actual, expected, "Should return 70")


if __name__ == "__main__":
    unittest.main(exit=False)
