#!/usr/bin/env python3

s = str(input())
note = " "
i = 0

while ord(note) > ord("g") or ord(note) < ord("a"):
    note = s[i]
    i += 1

print(note)
