#!/usr/bin/python
import sys
d=dict()
for line in sys.stdin:
    line=line.strip()
    time,count=line.split("\t")
    count=int(count)
    if time in d:
        d[time] = d[time] + count
    else:
        d[time] = count

for t in d:
    print t,"\t",d[t]
