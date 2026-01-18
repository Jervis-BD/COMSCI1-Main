#!/usr/bin/env python3

fig = int(input())

tens = (fig // 1000 % 10)
ones = fig // 100 % 10 * 10

print(tens + ones)
