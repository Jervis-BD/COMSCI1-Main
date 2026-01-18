#!/usr/bin/env python3

i = 0
negtotal = 0
postotal = 0

while i < 5:
    n = int(input())
    if n < 0:
        negtotal += n
    else:
        postotal += n
    i += 1
print(negtotal, postotal)
