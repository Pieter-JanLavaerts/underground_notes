#!/bin/python
from sys import argv

for l in open(argv[1]):
    ws = l.split(",")
    ts = ws[1:]
    for t in ts:
        try:
            int(t)
        except:
            print(t)

