#!/usr/bin/env python3

s = str(input())
last_digit = ""
i = 0
while i < len(s):
    if s[i] >= "0" and s[i] <= "9":
        last_digit = s[i]
    i += 1
if last_digit != "":
    print(last_digit)
