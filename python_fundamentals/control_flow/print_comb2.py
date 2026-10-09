#!/usr/bin/env python3

for value in range(100):
    ending = ", " if value < 99 else "\n"
    print("{0:02d}".format(value), end=ending)
