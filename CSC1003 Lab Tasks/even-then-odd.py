#!/usr/bin/env python3

i = input()
a = []
while i != "end":
    i = int(i)
    if i % 2 == 0:
        print(i)
    else:
        a.append(i)
    i = input()
i = 0
while i < len(a):
    print(a[i])
    i += 1
