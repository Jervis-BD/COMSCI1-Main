#!/usr/bin/env python3

import sys

lines = sys.stdin.read().rstrip().split()

i = 0
while i < len(lines):
    j = 1
    word = lines[i]
    while j < len(word) and ord(word[j - 1]) != ord(word[j]) - 1:
        j += 1
    if j < len(word):
        print(word)
    i += 1
