#!/usr/bin/env python3

homescore = int(input())
awayscore = int(input())

if homescore == awayscore:
    print("Draw.")
elif homescore > awayscore:
    print("Home win.")
else:
    print("Away win.")
