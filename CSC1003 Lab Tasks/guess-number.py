#!/usr/bin/env python3

import secret


max = 1000
min = 1
n = 500
guess = secret.guess(n)

while guess != "correct":
    if guess == "too-low":
        min = n
        n = (n + max) // 2
    elif guess == "too-high":
        max = n
        n = (n + min) // 2
    guess = secret.guess(n)
