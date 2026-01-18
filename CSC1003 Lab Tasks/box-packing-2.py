#!/usr/bin/env python3


boxes = 0
total = 0
n = int(input())
while n != 0:
    while total + n <= 1000 and n != 0:
        total += n
        n = int(input())
    boxes += 1
    total = 0
print(boxes)
