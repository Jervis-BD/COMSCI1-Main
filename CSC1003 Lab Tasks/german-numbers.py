#!/usr/bin/env python3

import sys
nums = sys.stdin.read().split()

trans = {
    "one": "eins",
    "two": "zwei",
    "three": "drei",
    "four": "vier",
    "five": "funf",
    "six": "sechs",
    "seven": "sieben",
    "eight": "acht",
    "nine": "neun",
    "ten": "zehn"
}

i = 0
while i < len(nums):
    print(trans[nums[i]])
    i += 1
