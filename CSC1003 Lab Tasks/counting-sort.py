#!/usr/bin/env python3

n = input()
a = [0] * 1000
while n != "end":
    n = int(n)
    a[n] += 1
    n = input()
i = 0
while i < len(a):
    if a[i] > 0:
        out = ("\n" + str(i)) * a[i]
        print(out[1:])
    i += 1
