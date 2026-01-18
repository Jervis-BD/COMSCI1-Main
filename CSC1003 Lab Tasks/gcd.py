#!/usr/bin/env python3

a = int(input())
b = int(input())

while b != 0:
    c = b
    b = a % b
    a = c
print(a)
