#!/usr/bin/env python3

out = 0

while out != 1000:
    s = input()
    i = 0
    while s[i] != "+":
        i += 1
    out = int(s[:i]) + int(s[i:])
    print(out)
