#!/usr/bin/env python3

prev = int(input())
n = 1
if prev != 0:
    while n != 0:
        n = int(input())
        if n != 0:
            if n > prev:
                print("higher")
            elif n == prev:
                print("equal")
            else:
                print("lower")
            prev = n
