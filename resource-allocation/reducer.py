#!/usr/bin/python
import sys
from decimal import Decimal

def reducer():
    recpower = 0
    prevKey = None
    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data)!=2:
            continue
        key, value = data #current key and value in the buffer stream

        if prevKey and prevKey!=key:
            print("{0}:{1}".format(prevKey, recpower))
            recpower = 0

        prevKey = key
        recpower += 1/Decimal(value)

    #for last key value pair
    if prevKey :
        print("{0}:{1}".format(prevKey, recpower))

if __name__ == "__main__":
    reducer()
