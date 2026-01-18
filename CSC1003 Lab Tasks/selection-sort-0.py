#!/usr/bin/env python3

n = input()
a = []
while n != "end":
    n = int(n)
    a.append(n)
    n = input()

i = 0
smallest = a[i]
while i < len(a):
    if a[i] < smallest:
        smallest = a[i]
    i += 1
print(smallest)
