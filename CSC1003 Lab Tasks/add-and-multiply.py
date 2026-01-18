#!/usr/bin/env python3

exp = input()
total = 0
tokens = exp.split("+")
tokensmult = []
i = 0
while i < len(tokens):
    if 1 < len(tokens[i].split("*")):
        tokensmult.append(tokens[i])
        tokens[i] = "0"
    i += 1
i = 0
while i < len(tokens):
    total += int(tokens[i])
    i += 1
i = 0
while i < len(tokensmult):
    j = 0
    temptotal = 1
    temp = tokensmult[i].split("*")
    while j < len(temp):
        temptotal *= int(temp[j])
        j += 1
    total += int(temptotal)
    i += 1
print(total)
