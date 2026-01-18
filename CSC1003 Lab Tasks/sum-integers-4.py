#!/usr/bin/env python3

import sys

args = sys.argv[1:]
i = 0
total = 0
while i < len(args):
    j = 0
    with open(args[i]) as f:
        file = f.read().split()
        while j < len(file) and len(file) > 1:
            total += int(file[j])
            j += 1

    i += 1
print(total)
