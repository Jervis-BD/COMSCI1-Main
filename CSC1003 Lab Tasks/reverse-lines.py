#!/usr/bin/env python3

s = str(input())
a = []
while s != "end":
    a.append(s)
    s = str(input())
i = 0
while i < len(a):
    print(a[len(a) - i - 1])
    i += 1
