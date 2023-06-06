#!/usr/bin/python3
for n in range(0, 100):
    if n >= 10:
        print("{}".format(n), end=', ')
    else:
        print("{:02}".format(n), end=', ')
