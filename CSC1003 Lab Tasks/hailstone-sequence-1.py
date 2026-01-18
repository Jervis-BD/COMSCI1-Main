#!/usr/bin/env python3

n = int(input())
m = int(input())
i = 0
print(m)

while i < n - 1:
    if m % 2 == 0:
        m = m // 2
        print(m)
    else:
        m = 3 * m + 1
        print(m)
    i += 1
