#!/bin/python
from sys import argv

for l in open(argv[1]):
    ws = l.split(",")
    ts = ws[1:]
    if len(ts) > 1:
        print(l)

