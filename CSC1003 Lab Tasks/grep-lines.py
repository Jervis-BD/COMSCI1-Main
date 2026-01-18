#!/usr/bin/env python3

import sys

pattern = sys.argv[1]
a = []
s = str(input())
i = len(pattern)
j = 0
include = 0
while s != "end":
    while i <= len(s):
        word = str(s[j:i])
        if word == pattern:
            include = 1
        j += 1
        i += 1
    if include == 1:
        a.append(s)
    include = 0
    s = str(input())
    j = 0
    i = len(pattern)

k = 0
while k < len(a):
    print(a[k])
    k += 1
