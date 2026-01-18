#!/usr/bin/env python3

i = 0
total = 0
n = int(input())
while total + n <= 1000:
    total += n
    n = int(input())
    i += 1
print(i)
