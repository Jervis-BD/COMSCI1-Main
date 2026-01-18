#!/usr/bin/env python3

smallestp = int(input())
i = 0

while i < 9:
    n = int(input())
    if n < smallestp and n > 0:
        smallestp = n
    i += 1

print(smallestp)
