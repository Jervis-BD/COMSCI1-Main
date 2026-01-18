#!/usr/bin/env python3

n = int(input())
p = int(input())

x = (n // (10 ** (p)))
y = x % 10
print(y)
