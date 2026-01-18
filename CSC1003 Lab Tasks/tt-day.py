#!/usr/bin/env python3

lines = input()
arr = []
while lines != "end":
    arr.append(lines)
    lines = input()

day = input()
i = 0

while i < len(arr):
    if arr[i][0] == day:
        print(arr[i])
    i += 1
