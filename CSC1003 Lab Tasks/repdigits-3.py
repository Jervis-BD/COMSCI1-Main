#!/usr/bin/env python3

output = ""
s = ""
while s != "end":
    s = str(input())
    if s[0] == s[1] and output == "":
        output = s
if len(output) > 0:
    print(output)
