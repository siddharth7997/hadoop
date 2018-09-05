#!/usr/bin/python
import sys
start=True
for line in sys.stdin:
    if not start:
        line=line.strip()
        words=line.split(",")
        print words[1].split(":")[0],"\t",1        
    else:
        start=False   