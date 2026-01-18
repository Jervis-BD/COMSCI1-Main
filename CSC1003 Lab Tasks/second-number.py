#!/usr/bin/env python3

s = str(input())
i = 0
n = 0
while n < 2:
    while i < len(s) and (s[i] < "0" or s[i] > "9"):
        i += 1
        start = i
    while i < len(s) and (s[i] >= "0" and s[i] <= "9"):
        i += 1
        end = i
    n += 1
if i < len(s) or (s[len(s) - 1] >= "0" and s[len(s) - 1] <= "9"):
    print(s[start:end], start)
