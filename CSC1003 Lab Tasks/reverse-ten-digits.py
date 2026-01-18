#!/usr/bin/env python3

i = 0
digits = 0
while i < 10:
    n = int(input()) * (10 ** i)
    digits += n
    i += 1
i = 0
while i < 10:
    d = (digits // (10 ** (9 - i))) % (10)
    print(d)
    i += 1
