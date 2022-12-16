"""
Author: IchBinJade
Date: 2022-12-16

Advent of Code 2022 - Day 2 Solution
https://adventofcode.com/2022/day/2
"""

import os
import time

def parse_input(path):
    with open(path) as file:
        inp = [line.strip(" ") for line in file]
    return inp


def part_one(input):
    # What would your total score be if everything goes exactly according to your strategy guide?
    combos = {"A Y":8, "A X":4, "A Z":3, "B Y":5, "B X":1, "B Z":9, "C Y":2, "C X":7, "C Z":6}
    total_score = 0
    for play in input:
        total_score += combos[play]

    return total_score


def part_two(input):
    # What's the revised total score
    combos = {"A Y":4, "A X":3, "A Z":8, "B Y":5, "B X":1, "B Z":9, "C Y":6, "C X":2, "C Z":7}
    total_score = 0
    for play in input:
        total_score += combos[play]

    return total_score
    

if __name__ == "__main__":
    t1 = time.time()

    # Get Input Data
    cwd = os.getcwd()
    path = cwd + "\day02.txt"
    with open(path) as file:
        inp_list = [line.strip() for line in file]
    
    # Get Solutions
    print(f"Part 1 = {part_one(inp_list)}")
    print(f"Part 2 = {part_two(inp_list)}")
    
    # Execution time
    t2 = time.time()
    print(f"\nExecution time = {t2 - t1:0.3f} seconds")
