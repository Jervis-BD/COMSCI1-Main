#!/usr/bin/env python3

x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

x3 = int(input())
y3 = int(input())

if x3 >= x2 and x3 >= x1:
    print("no")
elif y3 >= y2 and y3 >= y1:
    print("no")
elif x3 <= x2 and x3 <= x1:
    print("no")
elif y3 <= y2 and y3 <= y1:
    print("no")
else:
    print("yes")
