#!/usr/bin/env python3

import sys

file_name = sys.argv[1]
args = sys.argv[2:]
i = 0
##while i < len(args):
with open(file_name, "w") as f:
    while i < len(args):
        f.write(args[i] + "\n")
        i += 1
