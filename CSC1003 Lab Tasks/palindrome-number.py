#!/usr/bin/env python3

s = input()
n = int(s)
p = True
i = 0
while i < len(s):
    if (n // 10 ** (len(s) - 1 - i)) % 10 != (n // (10 ** i)) % 10:
        p = False
    i += 1
if p:
    print("yes")
else:
    print("no")
