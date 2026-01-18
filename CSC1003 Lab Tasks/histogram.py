#!/usr/bin/env python3

arr = [0] * 10

x = input()

while x != "end":
    x = int(x)

    arr[x] = int(arr[x]) + 1

    x = input()

i = 0

while i < 10:

    print(i, "*" * int(arr[i]))
    i += 1
