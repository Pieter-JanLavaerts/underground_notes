#!/usr/bin/env python3
from sys import argv
import subprocess

for l in open(argv[2]):
    try:
        ws = l.split(",")
        name = ws[0].replace(" ", "_").replace("(", "").replace(")", "").replace("/", "\\").replace("&", "")
        page = str(int(ws[1]))
        cmd = ["./pageToPng.sh", argv[1], page, name, argv[3]]
        print(cmd)
        subprocess.run(cmd)
    except Exception as e:
        print("Exception on line: ", l)
        print(e)
        raise

