#!/usr/bin/env python3

import sys
lines = sys.stdin.read().split()


i = 0
j = 0
while j < 3 and j < len(lines):
    i = j
    smallest = lines[j]
    smallpos = j
    while i < len(lines):
        if int(lines[i]) < int(smallest):
            smallest = lines[i]
            smallpos = i
        i += 1
    tmp = lines[j]
    lines[j] = smallest
    lines[smallpos] = tmp
    print(smallest)
    j += 1
