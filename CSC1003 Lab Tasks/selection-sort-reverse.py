#!/usr/bin/env python3

n = input()
a = []
while n != "end":
    n = int(n)
    a.append(n)
    n = input()

i = 0

while i < len(a):
    j = i
    smallpos = i
    while j < len(a):
        if a[smallpos] > a[j]:
            smallpos = j
        j += 1
    temp = a[smallpos]
    a[smallpos] = a[i]
    a[i] = temp
    i += 1

i = len(a)
while i > 0:
    print(a[i - 1])
    i -= 1
