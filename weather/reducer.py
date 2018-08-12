#!/usr/bin/python
import sys
from operator import itemgetter
d=dict()

for line in sys.stdin:
	line = line.strip()
	year,temp = line.split('\t',1)
	temp=float(temp)
	if year not in d:
		d[year]=temp
	else:
		if temp>d[year]:
			d[year]=temp
for k in d:
	print k,"\t",d[k]		
