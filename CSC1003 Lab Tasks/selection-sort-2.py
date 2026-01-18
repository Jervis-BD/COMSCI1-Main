#!/usr/bin/env python3

n = input()
a = []

while n != "end":
    n = int(n)
    a.append(n)
    n = input()

i = int(input())
small = a[i]
smallpos = i
while i < len(a):
    if small > a[i]:
        small = a[i]
        smallpos = i
    i += 1
print(smallpos)
