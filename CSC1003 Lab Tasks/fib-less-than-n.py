#!/usr/bin/env python3

n = int(input())
pv = 1
cv = 0

while cv < n:
    print(cv)
    cv = cv + pv
    pv = cv - pv
