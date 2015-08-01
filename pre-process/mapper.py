#!/usr/bin/python
import sys
def mapper():
    for line in sys.stdin:
        data = line.strip().split("::")
        if len(data)!=4:
            continue
        user, movie, rating, timestamp = data
        print("user{0}\t{1}".format(user,movie)) #to gather all users' item in reducer
        print("item{0}\t{1}".format(movie,user)) #to gather users of a particular item

if __name__ == "__main__":
    mapper()
