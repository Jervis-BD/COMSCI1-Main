#!/usr/bin/env python3

data = input()
while data != "end":
    i = 2
    while i < len(data) and data[i - 2:i] != "WI":
        i += 1
    if i < len(data):
        print(data[:i - 3])
    data = input()
