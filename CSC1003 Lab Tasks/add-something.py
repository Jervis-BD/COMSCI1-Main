#!/usr/bin/env python3

i = input()
a = []
while i != "end":
    i = int(i)
    a.append(i)
    i = input()

m = int(input())
i = 0
while i < len(a):
    print(a[i] + m)
    i += 1
