#!/usr/bin/env python3

data = input()
count = 0
while data != "end":
    i = 2
    while i < len(data) and data[i - 2:i] != "WI":
        i += 1
    if i < len(data):
        count += 1
    data = input()
print(count)
