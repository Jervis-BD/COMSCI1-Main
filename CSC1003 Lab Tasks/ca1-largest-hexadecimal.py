#!/usr/bin/env python3

hex1 = str(input())
hex2 = str(input())

if len(hex1) > len(hex2):
    print(hex1)
elif len(hex2) > len(hex1):
    print(hex2)

elif hex1 > hex2:
    print(hex1)
else:
    print(hex2)
