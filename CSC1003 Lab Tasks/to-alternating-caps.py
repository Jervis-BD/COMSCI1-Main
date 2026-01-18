#!/usr/bin/env python3

s = str(input())
i = 0
t = ""
p = 0
while i < len(s):
    c = s[i]
    lowerz = (ord(c) <= ord("z"))
    lowera = (ord(c) >= ord("a"))
    if (lowerz and lowera) or (ord(c) <= ord("Z") and ord(c) >= ord("A")):
        if p % 2 == 0:
            if ord(c) >= ord("a"):
                t += c
            else:
                t += chr(ord(c) + 32)
        else:
            if ord(c) >= ord("a"):
                t += chr(ord(c) - 32)
            else:
                t += c
        p += 1
    else:
        t += c
    i += 1
print(t)
