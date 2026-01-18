#!/usr/bin/env python3

s = str(input())
alpha = ""
while s != "end":
    i = 1
    while i < len(s) and s[i] >= s[i - 1]:
        i += 1
    if i == len(s):
        alpha = alpha + s + "\n"
    s = str(input())
print(alpha[:len(alpha) - 1])
