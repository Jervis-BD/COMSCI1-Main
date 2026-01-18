#!/usr/bin/env python3

import sys


height = int(input())
ant = int(input())

while height > 0:

    if height != ant and height != ant - 1:
        print((" " * (height) + "/").rstrip())
    else:
        print((" " * (height - 1) + "*/").rstrip())
    height -= 1
