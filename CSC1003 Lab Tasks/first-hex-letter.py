#!/usr/bin/env python3

n = int(input())
i = 1
hex_num = ""
power = 1
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


while i < len(hex_num) and (hex_num[i] < "a" or hex_num[i] > "f"):
    i += 1
if i < len(hex_num) and (hex_num[i] >= "a" and hex_num[i] <= "f"):
    print(hex_num[i])
