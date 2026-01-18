#!/usr/bin/env python3

s1 = int(input())
s2 = int(input())
s3 = int(input())

if s1 + s2 <= s3:
    print("no")
elif s2 + s3 <= s1:
    print("no")
elif s3 + s1 <= s2:
    print("no")
else:
    print("yes")
