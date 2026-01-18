#!/usr/bin/env python3

import sys

words = sys.stdin.read().split()
seen = {}
i = 0
while i < len(words) and (words[i] not in seen):
    seen[words[i]] = "snap"
    i += 1
if i < len(words):
    print("snap:", words[i])
