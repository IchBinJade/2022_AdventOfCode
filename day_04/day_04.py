"""
Author: IchBinJade
Date: 2023-02-04

Advent of Code 2022 - Day 4 Solution
https://adventofcode.com/2022/day/4
"""

import os
import time
import string

def is_range_a_in_range_b(first, second):
    first_a, first_b = map(int, first.split("-"))
    second_a, second_b = map(int, second.split("-"))
    if second_a <= first_a and first_b <= second_b:
        return True

def part_one(input):
    # In how many assignment pairs does one range fully contain the other?
    contained_count = 0
    for pairs in input:
        first_elf, second_elf = pairs.split(",")
        if is_range_a_in_range_b(first_elf, second_elf) or is_range_a_in_range_b(second_elf, first_elf):
            contained_count += 1

    return contained_count


if __name__ == "__main__":
    t1 = time.time()

    # Get Input Data
    cwd = os.getcwd()
    path = cwd + "/day04.txt"
    with open(path) as file:
        inp_list = [line.strip() for line in file]
    
    # Get Solutions
    print(f"Part 1 = {part_one(inp_list)}")
    
    # Execution time
    t2 = time.time()
    print(f"\nExecution time = {t2 - t1:0.3f} seconds")
