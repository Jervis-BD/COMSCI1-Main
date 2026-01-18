#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

vowel = "a e i o u A E I O U".split()
count = 0
i = 0
while i < len(lines):
    j = 0
    while j < len(lines[i]):
        if lines[i][j] in vowel:
            count += 1
        j += 1
    i += 1
print(count)
