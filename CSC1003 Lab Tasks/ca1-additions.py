#!/usr/bin/env python3

s = "0"

while s != "end":
    s = str(input())
    if s != "end":
        i = 0
        n = ""
        while i < len(s):
            if s[i] != " ":
                n += s[i]
            else:
                n1 = int(n)
                n = ""
            i += 1
        n2 = int(n)
        out = str(str(n1) + " + " + str(n2) + " = " + str(n1 + n2))
        while len(out) < 22:
            out = " " + out
        while out[20] != "=":
            out = " " + out
        print(out)
