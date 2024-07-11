#!/usr/bin/env python3
from sys import argv

for l in open(argv[1]):
    ws = l.split(",")
    ts = ws[1:]
    if len(ts) > 1:
        for t in ts:
            print(ws[0] + "," + t.replace("\n",""))
    else:
        print(l, end="")

