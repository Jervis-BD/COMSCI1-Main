#!/usr/bin/env python3

i = 0
smalleste = int(input())

while i < 9:
    n = int(input())
    if n % 2 == 0 and n < smalleste:
        smalleste = n
    i += 1
print(smalleste)
