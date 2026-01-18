#!/usr/bin/env python3

n = int(input())

sum = 1
i = 1

while i < n + 1:
    sum *= i
    i += 1
print(sum)
