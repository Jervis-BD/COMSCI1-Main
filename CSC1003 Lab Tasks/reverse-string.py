#!/usr/bin/env python3

s = str(input())
i = 0
t = ""
while i < len(s):
    t = s[i] + t
    i += 1
print(t)
