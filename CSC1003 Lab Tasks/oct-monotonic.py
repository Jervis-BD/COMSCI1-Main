#!/usr/bin/env python3

i = 0
oldn = 0
n = 0
while i < 16:
    if n >= oldn:
        oldn = n
    n = int(input())
    if n >= oldn:
        print(n)
    i += 1
