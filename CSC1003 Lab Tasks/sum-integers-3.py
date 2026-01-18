#!/usr/bin/env python3

import sys

i = 0
total = 0
args = sys.argv[1:]
while i < len(args):
    j = 0
    with open(args[i]) as f:
        file = f.read().split()
        while j < len(file):
            total += int(file[j])
            j += 1

    i += 1
print(total)
