#!/usr/bin/env python3

for value in range(ord("a"), ord("z") + 1):
    letter = chr(value)
    if letter in "eq":
        continue
    print("{}".format(letter), end="")
