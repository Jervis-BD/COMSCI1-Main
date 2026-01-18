#!/usr/bin/env python3

n = int(input())
i = 0
pwr2 = 0
binary = ""
while 2 ** (pwr2) < n:
    pwr2 = i + 1
    i += 1

i = 0

while pwr2 >= 0:
    if n - (2 ** pwr2) >= 0:
        binary += "1"
        n -= (2 ** pwr2)
    elif binary != "":
        binary += "0"
    pwr2 -= 1

print(binary)
