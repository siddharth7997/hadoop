#!/usr/bin/python
import sys
d=dict()
#linec=0
for line in sys.stdin:
    line = line.strip() #remove leading and trailing whitespaces
    site,count = line.split("\t")
    count=int(count)
    #print site,count
    #linec=linec+1
    if site not in d:
        d[site]=count
    else:
        d[site]=d[site]+count    
#print "Number of lines are",linec
for k in d:
    print k,"\t",d[k]
