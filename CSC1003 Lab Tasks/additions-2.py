#!/usr/bin/env python3

s = input()
i = 0
j = 0
out = 0

while i < len(s):
    while i < len(s) and s[i] != "+":
        i += 1
    num = int(s[j:i])
    out += num
    j = i + 1
    i += 1
print(out)
