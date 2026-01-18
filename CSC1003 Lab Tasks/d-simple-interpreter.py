#!/usr/bin/env python3

import sys

lines = sys.stdin.read().split("\n")
i = 0
var = [0] * 10
while i < len(lines) and lines[i] == "":
    i += 1
while i < len(lines):
    line = lines[i].split()

    if line[0] == "set":
        var[int(line[1][-1])] = line[2]

    elif line[0] == "print":
        print(var[int(line[1][-1])])

    elif line[0] == "add":
        arg1 = int(var[int(line[2][-1])])
        arg2 = int(var[int(line[3][-1])])
        var[int(line[1][-1])] = arg1 + arg2

    elif line[0] == "mult":
        arg1 = int(var[int(line[2][-1])])
        arg2 = int(var[int(line[3][-1])])
        var[int(line[1][-1])] = arg1 * arg2
    i += 1
    while i < len(lines) and lines[i] == "":
        i += 1
