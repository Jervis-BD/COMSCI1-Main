#!/usr/bin/env python3

s = str(input())
i = 0
capcount = 0
while i < len(s):
    if ord(s[i]) >= ord("A") and ord(s[i]) <= ord("Z"):
        capcount += 1
    i += 1
print(capcount)
