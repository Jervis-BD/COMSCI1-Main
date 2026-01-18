#!/usr/bin/env python3

s = str(input())
i = 0
start = 0
end = 0
while i < len(s) and (s[i] < "A" or s[i] > "Z"):
    i += 1
    start = i

while i < len(s) and (s[i] >= "A" and s[i] <= "Z"):
    i += 1
    end = i

if i < len(s) or (s[len(s) - 1] >= "A" and s[len(s) - 1] <= "Z"):
    print(s[start:end], start)
