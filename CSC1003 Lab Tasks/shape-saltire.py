#!/usr/bin/env python3

n = int(input())
i = 0
half = n // 2
while i < half:
    print(" " * i + "*" + " " * ((n - 2) - (i * 2)) + "*")
    i += 1

print(" " * half + "*")

i = 0
while i < half:
    print(" " * (half - i - 1) + "*" + " " * (2 * i + 1) + "*")
    i += 1
