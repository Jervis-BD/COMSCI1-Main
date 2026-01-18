#!/usr/bin/env python3

s = str(input())
i = 0
start = 0
end = len(s)
if s != "":
    while i < len(s):
        while i < len(s) and (s[i] < "0" or s[i] > "9"):
            i += 1
        if i < len(s):
            start = i
            #print(start, "start")
        while i < len(s) and (s[i] >= "0" and s[i] <= "9"):
            i += 1
        if i < len(s):
            end = i
            #print(end, "end")
        i += 1
    if s[start] >= "0" and s[start] <= "9":
        print(s[start:end])
