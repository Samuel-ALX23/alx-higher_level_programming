#!/usr/bin/python3
for lower_case in range(26):
  if lower_case != 4 and lower_case != 16:
    print("{}".format(chr(lower_case + ord("a"))), end="")
