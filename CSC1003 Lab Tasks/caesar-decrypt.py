#!/usr/bin/env python3

import sys

msg = sys.stdin.read().rstrip()
n = 13
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

trans = {}
enc = ""

src = lower + upper
dst = lower[n:] + lower[:n] + upper[n:] + upper[:n]
i = 0
while i < len(src):
    trans[dst[i]] = src[i]
    i += 1
i = 0
while i < len(msg):
    if msg[i] in trans:
        enc += trans[msg[i]]
    else:
        enc += msg[i]
    i += 1
print(enc)
