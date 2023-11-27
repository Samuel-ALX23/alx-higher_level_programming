#!/usr/bin/python3
add_numbers = __import__('0-add_integer').add_numbers

print(add_numbers(1, 2))
print(add_numbers(100, -2))
print(add_numbers(2))
print(add_numbers(100.3, -2))
try:
    print(add_numbers(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_numbers(None))
except Exception as e:
    print(e)
