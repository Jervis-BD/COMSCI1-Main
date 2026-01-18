#!/usr/bin/env python3

s = input()
a = []
count = 0
while s != "end":
    a.append(s)
    s = input()
    count += 1
i = 0
while i < len(a):
    print(i, count, a[i])
    i += 1
