#!/usr/bin/env python3

s1 = str(input())
s2 = str(input())
s3 = str(input())

if len(s1) > len(s2) and len(s1) > len(s3):
    print(s1)
elif len(s2) > len(s3):
    print(s2)
else:
    print(s3)
