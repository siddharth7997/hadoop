#!/usr/bin/python
import sys
import re
for line in sys.stdin:
    line = line.strip() #remove leading and trailing whitespaces
    # words = line.split("\"") #split the line into words and returns as a list
    # for m in words:
    #     if "https://" in m or "http://" in m:
    #         print m,"\t",1
    urls = re.findall('https?://(?:[-\w.\/])+',line)
    if urls:
        print urls[0],"\t",1

