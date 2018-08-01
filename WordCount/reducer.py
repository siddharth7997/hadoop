#!/usr/bin/python
import sys
from operator import itemgetter
d=dict()
for line in sys.stdin:
	line = line.strip()
	word,count = line.split('\t',1)
	#print word,count
	
	if word not in d:
		d[word]=1
	else:
		d[word]=d[word]+1
for j in d:
	print j,"\t",d[j]		 
