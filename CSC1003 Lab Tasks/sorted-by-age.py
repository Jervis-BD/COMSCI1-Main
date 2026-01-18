#!/usr/bin/env python3

n = str(input())
dob = []
name = []
while n != "end":

    dob.append(n[:8])
    name.append(n[9:])
    n = input()

i = 0

while i < len(dob):
    j = i
    smallpos = i
    while j < len(dob):
        if dob[smallpos][7:] > dob[j][7:]:
            smallpos = j
        j += 1
    temp = dob[smallpos]
    temp2 = name[smallpos]

    dob[smallpos] = dob[i]
    name[smallpos] = name[i]
    dob[i] = temp
    name[i] = temp2
    i += 1
i = 0
while i < len(name):
    print(name[i])
    i += 1


