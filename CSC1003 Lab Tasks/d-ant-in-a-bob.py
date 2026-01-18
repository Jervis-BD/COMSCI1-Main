#!/usr/bin/env python3


length = int(input())
ant = int(input())

print("\\")
print(" \\")


i = 0
while i < length:
    if length - i == ant or length - i == ant - 1:
        print(" " * i + "\\*\\")
    else:
        print(" " * i + "\\ \\")
    i += 1
