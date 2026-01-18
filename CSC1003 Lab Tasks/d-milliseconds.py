#!/usr/bin/env python3

import sys

times = sys.stdin.readlines()

i = 0
while i < len(times):
    j = 1
    line = times[i]
    while line[j] != " ":
        j += 1
    days = int(line[:j])
    line = line[j + 1:]
    j = 1
    while line[- j] != ".":
        j += 1
    miliseconds = line[- j + 1:].rstrip()
    line = line[: - j]
    line = line.split(":")
    line = [days, int(line[0]), int(line[1]), int(line[2]), int(miliseconds)]

    #yes i hate this
    while len(str(line[4])) < 3 and line[4] != 0:
        line[4] *= 10
    miliseconds = 0

    miliseconds += line[0] * 24 * 60 * 60 * 1000
    miliseconds += line[1] * 60 * 60 * 1000
    miliseconds += line[2] * 60 * 1000
    miliseconds += line[3] * 1000
    miliseconds += line[4]
    print(miliseconds)
    i += 1
