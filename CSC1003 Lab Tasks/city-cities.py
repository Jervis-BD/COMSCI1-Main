#!/usr/bin/env python3

data = input()
data = input()
while data != "end":
    i = 0
    while data[i] != ",":
        i += 1
    if data[i - 4:i] == "City":
        print(data[:i])
    data = input()
