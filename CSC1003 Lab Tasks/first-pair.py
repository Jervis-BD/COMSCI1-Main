#!/usr/bin/env python3

s = str(input())
i = 1

while i < len(s) and s[i] != s[i - 1]:
    i += 1

if i < len(s) and i > 0:
    print(s[i] * 2)
