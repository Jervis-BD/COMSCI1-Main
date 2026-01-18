#!/usr/bin/env python3

s = str(input())
i = 0
t = ""
while i < len(s):
    if s[i] != " ":
        t += s[i]
    i += 1
print(t)
