#!/usr/bin/env python3

s = str(input())
i = 0
sum = 0
while i < len(s):
    n = s[i]
    sum += int(n)
    i += 1
print(sum)
