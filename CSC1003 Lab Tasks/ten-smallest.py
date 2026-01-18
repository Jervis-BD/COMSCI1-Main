#!/usr/bin/env python3

i = 0
smallest = int(input())

while i < 9:
    n = int(input())
    if smallest > n:
        smallest = n
    i += 1
print(smallest)
