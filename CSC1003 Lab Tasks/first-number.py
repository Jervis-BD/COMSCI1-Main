#!/usr/bin/env python3

s = str(input())
i = 0
n = ""
while i < len(s) and (s[i] < "0" or s[i] > "9"):
    i += 1
appear = i
while i < len(s) and (s[i] > "0" and s[i] < "9"):
    n += s[i]
    i += 1

if i < len(s):
    print(n, appear)
