#!/usr/bin/python3
for lower_case in range(97, 123):
  if chr(lower_case) != "q" and chr(lower_case) != "e":
    print("{}".format(chr(lower_case)), end="")
