#!/usr/bin/env python3

f = str(input())
i = 0
start = 0
end = 0
while i < len(f) and f[i] != ".":
    i += 1
end = i


print(f[:end])
print(f[end + 1:])
