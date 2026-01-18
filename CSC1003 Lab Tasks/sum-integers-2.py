#!/usr/bin/env python3

import sys
nums = sys.argv[1]
total = 0
i = 0
with open(nums) as f:
    #print(f.read().rstrip())
    file = f.read().rstrip()
    arr = file.split("\n")
    while i < len(arr) and len(arr) > 1:
        total += int(arr[i])
        i += 1
print(total)
