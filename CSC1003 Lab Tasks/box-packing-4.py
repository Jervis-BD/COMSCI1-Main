#!/usr/bin/env python3

n = input()
subtot = 0
while n != "end":
    if n == "0":
        n = int(n)
        perc = subtot // 10
        print(str(perc) + "%")
        subtot = 0
    subtot += int(n)
    n = input()
