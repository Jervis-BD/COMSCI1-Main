#!/usr/bin/env python3

import sys

lines = sys.stdin.read().rstrip().split("\n")
count = 0
i = 0
while i < len(lines):
    mark = lines[i].split()
    #print(mark)
    count += int(mark[2])
    i += 1

average = count // i
i = 0
while i < len(lines):
    mark = lines[i].split()
    if average < int(mark[2]):
        print(mark[0], mark[1])
    i += 1
