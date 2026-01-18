#!/usr/bin/env python3

weight = input()
a = []
while weight != "end":
    weight = int(weight)
    a.append(weight)
    weight = input()
i = 0

while i < len(a):
    p = i
    j = i + 1
    while j < len(a):
        if a[j] < a[p]:
            p = j
        j = j + 1

    tmp = a[p]
    a[p] = a[i]
    a[i] = tmp

    i = i + 1
i = 0
total = 0
while total + a[i] < 500:
    total += a[i]
    i += 1
print(i, total)
