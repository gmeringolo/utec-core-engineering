#!/usr/bin/env python3
safe_print_integer = __import__('safe_print_integer').safe_print_integer

value = 24
print(safe_print_integer(value))

value = "School"
print(safe_print_integer(value))
