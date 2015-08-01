#!/usr/bin/python
import sys

def reducer():
    prevKey = None
    recdict = {}
    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data)!=2:
            continue
        key, value = data #current key and value in the buffer stream
        
        if prevKey and prevKey!=key:
            prevKey = int(prevKey)
            print("{0}::{1}".format(prevKey, recdict))
            recdict.clear()

        prevKey = key
        item, power = list(map(float, value.split(",")))

        if item in recdict:
            recdict[item] += power
        else:
            recdict[item] = power

    #for last key value pair
    if prevKey :
        prevKey = int(prevKey)
        print("{0}::{1}".format(prevKey, recdict))

if __name__ == "__main__":
    reducer()
