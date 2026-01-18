#!/usr/bin/env python3

lines = input()

while lines != "end":
    tokens = lines.split()
    print(" ".join(tokens[5:]))
    lines = input()
