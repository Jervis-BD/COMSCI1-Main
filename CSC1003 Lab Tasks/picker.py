#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())

cparity = c % 2
cparityp1 = ((c + 1) % 2)
print(cparity * b + a * cparityp1)
