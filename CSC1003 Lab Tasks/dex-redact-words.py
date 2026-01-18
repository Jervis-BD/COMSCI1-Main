#!/usr/bin/env python3

import sys

banned = {}
i = 0
args = sys.argv
while i < len(args):
    banned[args[i]] = True
    i += 1

lines = sys.stdin.read().split()
i = 0
while i < len(lines):
    if lines[i] in banned:
        lines[i] = "*" * len(lines[i])
    print(lines[i])
    i += 1
