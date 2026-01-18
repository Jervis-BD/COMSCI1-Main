#!/usr/bin/env python3

import sys

a = sys.stdin.read().split()
i = 0
while i < len(a):
    string = a[i]
    arr = string.split("/")
    print(arr[-1])
    i += 1
