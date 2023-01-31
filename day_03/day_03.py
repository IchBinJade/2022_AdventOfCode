"""
Author: IchBinJade
Date: 2023-01-31

Advent of Code 2022 - Day 3 Solution
https://adventofcode.com/2022/day/3
"""

import os
import time
import string

def part_one(input):
    # What is the sum of the priorities of those item types?
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    priority = 0
    total_priority = 0

    for rucksack in input:
        half = len(rucksack)//2
        comp_one = set(rucksack[:half])
        comp_two = set(rucksack[half:])
        common = next(iter(comp_one.intersection(comp_two)))
        if common in lowers:
            priority = 1 + lowers.index(common)
        elif common in uppers:
            priority = 27 + uppers.index(common)
        
        total_priority += priority

    return total_priority


if __name__ == "__main__":
    t1 = time.time()

    # Get Input Data
    cwd = os.getcwd()
    path = cwd + "\day03.txt"
    with open(path) as file:
        inp_list = [line.strip() for line in file]
    
    # Get Solutions
    print(f"Part 1 = {part_one(inp_list)}")
    
    # Execution time
    t2 = time.time()
    print(f"\nExecution time = {t2 - t1:0.3f} seconds")
