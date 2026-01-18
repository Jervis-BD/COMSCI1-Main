#!/usr/bin/env python3

s = str(input())

day = ""
date = ""
month = ""
year = ""
j = 0


while s[j] != " ":
    day += s[j]
    j += 1
j += 1

while s[j] != " ":
    date += s[j]
    j += 1
j += 1

while s[j] != ",":
    month += s[j]
    j += 1
j += 2

year = s[j:]

print(month, date + ",", year, "(" + day + ")")
