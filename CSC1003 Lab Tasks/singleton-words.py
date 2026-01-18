#!/usr/bin/env python3

import sys

lines = sys.stdin.read().split()
out = []
i = 0
while i < len(lines):
    j = 0
    same = False
    while j < len(lines):
        if lines[i] == lines[j] and i != j:
            same = True
        j += 1
    if not same:
        out.append(lines[i])
    i += 1
i = 0
while i < len(out):
    print(out[i])
    i += 1
