#!/usr/bin/env python3

n = int(input())
i = 0
while i * i < n:
    highestsquare = i * i
    i += 1
print(highestsquare)
