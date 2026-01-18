#!/usr/bin/env python3

s = str(input())
i = 0
out = ""
while i < len(s):
    if s[i] >= "a" and s[i] <= "z":
        out += chr(ord(s[i]) - 32)
    else:
        out += s[i]
    i += 1
print(out)
