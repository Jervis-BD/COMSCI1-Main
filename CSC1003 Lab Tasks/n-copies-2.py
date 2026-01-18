#!/usr/bin/env python3

s = str(input())
n = int(input())

out = ((s + "-") * n)
print(out[0:len(out) - 1])
