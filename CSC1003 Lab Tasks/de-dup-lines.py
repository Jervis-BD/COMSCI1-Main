#!/usr/bin/env python3

line = input()
seen = []
while line != "end":
    i = 0
    while i < len(seen) and seen[i] != line:
        i += 1

    if i >= len(seen):
        seen.append(line)
        print(line)

    line = input()
