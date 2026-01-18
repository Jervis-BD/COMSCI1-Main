#!/usr/bin/env python3

n = 1
i = 0
total = 0
while n != 0:
    n = int(input())
    if n < 0:
        n *= - 1
    total += n
    i += 1
print(total)
