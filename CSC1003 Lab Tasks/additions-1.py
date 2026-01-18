#!/usr/bin/env python3

j = 0
while j < 10:
    s = input()
    i = 0
    while s[i] != "+":
        i += 1
    out = int(s[:i]) + int(s[i:])
    print(out)
    j += 1
