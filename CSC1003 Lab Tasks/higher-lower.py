#!/usr/bin/env python3

prev = int(input())
i = 0

while i < 5:
    n = int(input())
    if n > prev:
        print("higher")
    elif n == prev:
        print("equal")
    else:
        print("lower")
    prev = n
    i += 1
