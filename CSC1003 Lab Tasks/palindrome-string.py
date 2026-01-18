#!/usr/bin/env python3

s = str(input())
i = 0

while i < len(s) and s[i] == s[len(s) - i - 1]:
    i += 1

if i == len(s) and s != "":
    print("palindrome")
