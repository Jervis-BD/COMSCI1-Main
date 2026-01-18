#!/usr/bin/env python3

n = input()
arr = []
servers = 0
i = 0

while n != "end":
    n = int(n)
    arr.append(n)
    n = input()

while i < len(arr):
    live_servers = 0
    j = i
    while j < len(arr):
        if arr[i] + 1000 > arr[j]:
            live_servers += 1
        j += 1

    if live_servers > servers:
        servers = live_servers
    i += 1

print(servers)
