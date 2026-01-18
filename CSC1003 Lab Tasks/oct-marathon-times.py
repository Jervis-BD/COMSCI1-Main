#!/usr/bin/env python3

s = ""
count = 0
seconds = 0
minutes = 0
hours = 0

while s != "end":
    s = str(input())
    if s != "end":
        count += 1
        i = 0
        temphours = ""
        tempminutes = ""
        tempseconds = ""
        while i < len(s) and s[i] != ":":
            temphours += s[i]
            i += 1
        hours += int(temphours)
        i += 1
        while i < len(s) and s[i] != ":":
            tempminutes += s[i]
            i += 1
        minutes += int(tempminutes)
        i += 1
        while i < len(s) and s[i] != ":":
            tempseconds += s[i]
            i += 1
        seconds += int(tempseconds)

seconds += hours * 60 * 60
seconds += minutes * 60
hours = 0
minutes = 0

seconds = seconds // count
while seconds >= 60:
    seconds -= 60
    minutes += 1
while minutes >= 60:
    minutes -= 60
    hours += 1
if len(str(seconds)) < 2:
    seconds = "0" + str(seconds)
if len(str(minutes)) < 2:
    minutes = "0" + str(minutes)

print(str(hours) + ":" + str(minutes) + ":" + str(seconds))
