#!/usr/bin/env python3

lines = input()

while lines != "end":
    tokens = lines.split()
    if int(tokens[2]) > 1:
        print(" ".join(tokens))
    lines = input()
