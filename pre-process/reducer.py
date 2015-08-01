#!/usr/bin/python
import sys
from pymongo import MongoClient

def reducer():
    allValues = ""
    prevKey = None
    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data)!=2:
            continue
        key, value = list(map(str,data)) #current key and value in the buffer stream
        #value = str(value)
        if prevKey and prevKey!=key:
            if prevKey.startswith("item"):
                #write to any db, we will use mongoDB or Cassandra
                #we are using mongoDB as our real-time storage

                item = prevKey.split("item")
                iid = int(item[1]) #item id
                userlist = list(map(int, allValues.split(";"))) #creating py list of all users using this item
                doc = {"iid":iid, "userlist":userlist}
                
                #insert doc document in items collection
                db.items.insert_one(doc)

            if prevKey.startswith("user"):
                #write to any db, we will use mongoDB or Cassandra
                #we are using mongoDB as our real-time storage

                user = prevKey.split("user")
                uid = int(user[1]) #user id
                itemlist = list(map(int, allValues.split(";"))) #creating py list of all items of this user
                doc = {"uid":uid, "itemlist":itemlist}

                #insert doc document in users collection
                db.users.insert_one(doc)

                #print userx:itemlist to hdfs
                print("{0}:{1}".format(prevKey, allValues))
                
            allValues = ""
        
        #previous key is same key
        prevKey = key
        #if this key came for first time
        if allValues == "" :
            allValues = value
        else: #concatenate values for same key
            allValues = allValues + ";" + value
    
    #for last key value
    if prevKey :
        if prevKey.startswith("item"):
            #write to any db, we will use mongoDB or Cassandra
            #we are using mongoDB as our real-time storage

            item = prevKey.split("item")
            iid = int(item[1]) #item id
            userlist = list(map(int, allValues.split(";"))) #creating py list of all users using this item
            doc = {"iid":iid, "userlist":userlist}
            
            #insert doc document in items collection
            db.items.insert_one(doc)

        if prevKey.startswith("user"):
            #write to any db, we will use mongoDB or Cassandra
            #we are using mongoDB as our real-time storage

            user = prevKey.split("user")
            uid = int(user[1]) #user id
            itemlist = list(map(int, allValues.split(";"))) #creating py list of all items of this user
            doc = {"uid":uid, "itemlist":itemlist}

            #insert doc document in users collection
            db.users.insert_one(doc)

            #print userx:itemlist to hdfs
            print("{0}:{1}".format(prevKey, allValues))

if __name__ == "__main__":
    client = MongoClient()
    db = client['recengine']
    reducer()
