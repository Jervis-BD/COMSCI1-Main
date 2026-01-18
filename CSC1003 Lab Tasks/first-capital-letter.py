#!/usr/bin/env python3

s = str(input())
i = 0
firstcap = " "
while ord(firstcap) > ord("Z") or ord(firstcap) < ord("A"):
    firstcap = s[i]
    i += 1
print(i - 1)
