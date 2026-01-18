#!/usr/bin/env python3

data = input()
k = 0
j = 0
while j < len(data):
    while j < len(data) and data[j] != ",":
        j += 1
    print(data[k:j])
    j += 1
    k = j
