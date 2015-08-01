#!/usr/bin/python
import sys
def mapper():
    for line in sys.stdin:
        data = line.strip().split(":")
        if len(data)!=2:
            continue
        user, itemlist = data
        itemlist = itemlist.split(";")
        totalItems = len(itemlist)
        for i in range(totalItems):
        	if i+1 >= totalItems:
        		break
        	for j in range(i+1, totalItems):
        		if int(itemlist[i]) <=  int(itemlist[j]):
        			print("{0}_{1}\t{2}".format(itemlist[i], itemlist[j], totalItems))
        		else:
        			print("{0}_{1}\t{2}".format(itemlist[j], itemlist[i], totalItems))

if __name__ == "__main__":
    mapper()
