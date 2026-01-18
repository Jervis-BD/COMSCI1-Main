#!/usr/bin/env python3

lines = input()

while lines != "end":
    tokens = lines.split()
    if tokens[1][0] == "0":
        tokens[1] = tokens[1][1:]
    tokens[2] = str((int(tokens[1]) - 1 + int(tokens[2])) % 23)
    tokens[1] = tokens[1] + ":00"
    tokens[2] = tokens[2] + ":50"
    print(" ".join(tokens))
    lines = input()
