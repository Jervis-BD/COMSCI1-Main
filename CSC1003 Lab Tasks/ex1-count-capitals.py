#!/usr/bin/env python3

i = 0
s = str(input())
count = 0
while i < len(s):
    if s[i] >= "A" and s[i] <= "Z":
        count += 1
    i += 1
print(count)
