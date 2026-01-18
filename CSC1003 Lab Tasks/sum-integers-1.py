#!/usr/bin/env python3

import sys

a = sys.stdin.read().split()
i = 0
total = 0
while i < len(a):
    total += int(a[i])
    i += 1
print(total)
