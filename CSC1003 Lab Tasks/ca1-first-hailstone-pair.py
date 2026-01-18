#!/usr/bin/env python3

state = 1
oldn = int(input())
while state == 1:
    n = int(input())
    if oldn % 2 == 0:
        if oldn // 2 == n:
            print(oldn, n)
            state = 0
    else:
        if oldn * 3 + 1 == n:
            print(oldn, n)
            state = 0
    oldn = n
