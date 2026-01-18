#!/usr/bin/env python3

f = str(input())
i = 0
j = 0
if f[j] == ".":
    print("0" + f)

elif f[-1] == ".":
    print(f + "0")
elif f[j] == "-" and f[j + 1] == ".":
    print("-" + "0" + f[1:])
else:
    while i + 1 < len(f) and f[i] != ".":
        i += 1
    if f[i] != ".":
        print(f + ".0")
    else:
        print(f)
