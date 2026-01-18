#!/usr/bin/env python3

import sys

items = sys.stdin.read().split("\n")
fruit = {
    "apple": True,
    "pear": True,
    "orange": True,
    "banana": True,
    "cherry": True,
}
i = 0
while i < len(items):
    if items[i] in fruit:
        print(items[i])
    i += 1
