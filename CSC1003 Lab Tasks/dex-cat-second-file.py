#!/usr/bin/env python3

import sys

file1 = sys.argv[1]


with open(file1) as f:
    file2 = f.read().rstrip()

with open(file2) as f:
    print(f.read().rstrip())
