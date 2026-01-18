#!/usr/bin/env python3

n = input()
a = []
while n != "end":
    n = int(n)
    a.append(n)
    n = input()

i = 0
posmol = i
while i < len(a):
    if a[i] < a[posmol]:
        posmol = i
    i += 1
print(posmol)
