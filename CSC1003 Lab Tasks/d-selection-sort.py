#!/usr/bin/env python3

import sys

lines = sys.stdin.read().split()
#print(lines)

i = 0


while i < 5:
    j = i + 1
    smallest = lines[j]
    smallpos = j
    while j < len(lines):
        if int(lines[j]) < int(smallest):
            smallest = lines[j]
            smallpos = j
        j += 1
    tmp = lines[i]
    lines[i] = smallest
    lines[smallpos] = tmp
    i += 1

i = 0
while i < len(lines):
    print(lines[i])
    i += 1
