#!/usr/bin/python3
print_name = __import__('3-say_my_name').print_name

print_name("John", "Smith")
print_name("Walter", "White")
print_name("Bob")
try:
    print_name(12, "White")
except Exception as e:
    print(e)
