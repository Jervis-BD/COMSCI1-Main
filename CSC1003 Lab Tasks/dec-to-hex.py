#!/usr/bin/env python3

n = int(input())
i = 1
power = 1
hex_num = ""
while n > power:
    power = 16 ** i
    i += 1

string = "0123456789abcdef"

while n > 0:
    hex_digit = n // 16 ** (i - 1)

    n = n % (16 ** (i - 1))

    hex_num += string[hex_digit]

    i -= 1
if hex_num[0] == "0":
    hex_num = hex_num[1:]
print(hex_num)
