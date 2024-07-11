#!/usr/bin/env python3
from sys import argv
from os import system

for l in open(argv[1]):
    try:
        ws = l.split(",")
        name = ws[0].replace(" ", "_").replace("(", "").replace(")", "").replace("/", "\\").replace("&", "")
        page = str(int(ws[1]))
        cmd = "./pageToPng.sh " + page + " " + name + " " + argv[2]
        system(cmd)
    except Exception as e:
        print("Exception on line: ", l)
        print(e)
        raise

