#!/usr/bin/env python3

count = 0
longest = 0
n = input()
prev = n
longest_sequence = ""
running_sequence = ""
while n != "end":
    n = int(n)
    prev = int(prev)
    if n >= prev:
        count += 1
        running_sequence = running_sequence + str(n) + "\n"
        if count > longest:
            longest_sequence = running_sequence
            longest = count
    else:
        count = 1
        running_sequence = str(n) + "\n"
    prev = n
    n = input()

##longest_sequence = longest_sequence + "\n" + str(curr)
if len(longest_sequence) > 0:
    print(longest_sequence[:len(longest_sequence) - 1])
