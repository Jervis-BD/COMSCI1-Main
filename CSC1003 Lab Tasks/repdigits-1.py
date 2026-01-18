#!/usr/bin/env python3

i = 0
output = ""
n = int(input())
while i < n:
    s = str(input())
    if s[0] == s[1]:
        output = output + s + "\n"
    i += 1
print(output[: - 1])
