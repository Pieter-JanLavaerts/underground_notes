#!/bin/python
from sys import argv

i = 0
for l in open(argv[1]):
    i += 1
    ws = l.split(",")
    ts = ws[1:]
    for t in ts:
        try:
            int(t)
        except:
            print(i, t)

