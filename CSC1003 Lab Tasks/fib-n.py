#!/usr/bin/env python3

n = int(input())
i = 0
pv = 1
cv = 0

while i < n:
    print(cv)
    cv = cv + pv
    pv = cv - pv
    i += 1
