"""
Author: IchBinJade
Date: 2022-12-15

Advent of Code 2022 - Day 1 Solution
https://adventofcode.com/2022/day/1
"""

import unittest
from day_01 import part_one, part_two

class TestDay01(unittest.TestCase):

    def test_part_one(self):
        input = [1000,2000,3000,"",4000,"",5000,6000,"",7000,8000,9000,"",10000]
        actual = part_one(input)
        expected = 24000
        self.assertEqual(actual, expected, "Should return 24000")

    def test_part_two(self):
        input = [1000,2000,3000,"",4000,"",5000,6000,"",7000,8000,9000,"",10000,""]
        actual = part_two(input)
        expected = 45000
        self.assertEqual(actual, expected, "Should return 45000")
        return


if __name__ == "__main__":
    unittest.main(exit=False)
