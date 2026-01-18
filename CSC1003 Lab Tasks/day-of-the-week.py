#!/usr/bin/env python3

month = int(input())
day = int(input())
date = day + ((month - 1) * 30)
wkday = (date - 1) % 7
print(wkday + 1)
