#!/usr/bin/python3
for b in range(100):
    if b == 99:
        print(b)
    else:
        print("{}".format('0' + str(b) if b < 10 else b), end=", ")
