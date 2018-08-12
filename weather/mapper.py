#!/usr/bin/python
import sys
#Word Count Example
# input comes from standard input STDIN
for line in sys.stdin:
	line = line.strip() #remove leading and trailing whitespaces
	year=line[15:19]
	temp=float(line[87:92])/10
	quality=line[92:93]
	if temp!=9999 and quality in "[01459]":
		print year,"\t",temp

