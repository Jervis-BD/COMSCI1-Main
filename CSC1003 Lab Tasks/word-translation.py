#!/usr/bin/env python3

import sys

nums = sys.stdin.read().split()


with open("translation.txt") as f:
    i = 0
    trans = f.read().split("\n")
    while i < len(nums):
        j = 0
        d = trans[j].split()
        while d[0] != nums[i]:
            j += 1
            d = trans[j].split()
        print(d[1])
        i += 1
