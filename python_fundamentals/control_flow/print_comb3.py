#!/usr/bin/env python3

for left in range(10):
    for right in range(left + 1, 10):
        if left == 8:
            print("{}{}".format(left, right))
        else:
            print("{}{}".format(left, right), end=", ")
