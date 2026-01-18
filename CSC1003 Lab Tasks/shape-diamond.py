#!/usr/bin/env python3

n = int(input())
i = 0
half = n // 2
star = "*"
while i < half:
    print(" " * (half - i - 1), star)
    i += 1
    star += "**"
print("*" * n)
while i > 0:
    i -= 1
    star = star[:len(star) - 2]
    print(" " * (half - i - 1), star)
