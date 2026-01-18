#!/usr/bin/env python3

count = 0
longest = 0
n = input()
prev = n
while n != "end":
    n = int(n)
    prev = int(prev)
    if n >= prev:
        count += 1
        if count >= longest:
            longest = count
    else:
        count = 1
    prev = n
    n = input()
print(longest)
