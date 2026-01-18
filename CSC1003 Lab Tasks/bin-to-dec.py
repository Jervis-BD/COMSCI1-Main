#!/usr/bin/env python3

s = str(input())
length = int(len(s))
i = 0
decimal = 0

while i < length:
    digit = int(s[i])
    decimal += digit * (2 ** (length - i - 1))
    i += 1
print(decimal)
