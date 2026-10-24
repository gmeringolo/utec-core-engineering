#!/usr/bin/env python3

from calculator_1 import suma, resta, multi, divi

if __name__ == "__main__":
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, suma(a, b)))
    print("{} - {} = {}".format(a, b, resta(a, b)))
    print("{} * {} = {}".format(a, b, multi(a, b)))
    print("{} / {} = {}".format(a, b, divi(a, b)))
