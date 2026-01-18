#!/usr/bin/env python3

i = 0
output = ""
while output == "":
    n = int(input())
    if n % 5 == 0 and n % 3 == 0 and output == "":
        output = n
    i += 1
print(output)
