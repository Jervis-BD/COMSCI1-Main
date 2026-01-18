#!/usr/bin/env python3

import sys
args = sys.argv

with open(args[1]) as f:
    atxt = f.read()
with open(args[2]) as f:
    btxt = f.read()
with open(args[1], "w") as f:
    f.write(btxt)
with open(args[2], "w") as f:
    f.write(atxt)
