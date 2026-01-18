#!/usr/bin/env python3

s = str(input())
start = 0
end = 1
alpha = ""
include = 1
while s != "end":
    while end < len(s):
        while end < len(s) and s[end] != " ":
            if s[end] < s[end - 1] and s[end - 1] != " ":
                include = 0
            end += 1
        if include == 1:
            alpha = alpha + s[start:end] + "\n"

        end += 1
        start = end
        include = 1
    if len(s) < 2:
        alpha = alpha + s + "\n"
    s = str(input())
    end = 1
    start = 0

print(alpha[:len(alpha) - 1])
