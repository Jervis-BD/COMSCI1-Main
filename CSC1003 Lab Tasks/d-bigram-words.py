#!/usr/bin/env python3

import sys
lines = sys.stdin.read().split()
i = 0
count = []
bigrams = {}
bic = 0

#### read all bigrams to a dictionary and have their translation specify
#### a position in a list which refers to their frequence
#### ie if its new write to dict --> else add to its counter


while i < len(lines):
    j = 0
    while j < len(lines[i]):
        s = lines[i][j: j + 2]
        if s not in bigrams:
            bigrams[s:bic]
            bic += 1
            count.append[1]
        else:
            count[bigrams[s]] = count[bigrams[s]] + 1
        j += 1
    i += 1


#### now find biggest element of count
i = 0
biggest = i
while i < len(count):
    if count[biggest] < count[i]:
        biggest = i
    i += 1

bigram = bigrams[biggest]
#### now re search all lines for those which include the most common
i = 0
out = []
while i < len(lines):
    j = 0
    include = False
    while j < len(lines[i]):
        s = lines[i][j: j + 2]
        if s == bigram:
            include == True
    if include:
        out.append[lines[i]]
    i += 1

i = 0
while i < len(out):
    print(out[i])
    i += 1
#### obviously if bigram is tied for most common this doesnt work


        
