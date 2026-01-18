#!/usr/bin/env python3

output = ""
while output == "":
    s = str(input())
    if s[0] == s[1]:
        output = s
print(output)
