from pymongo import MongoClient
import json
import os
from auth import MONGODB_URI

DBS_NAME = "first_mongodb"
COLLECTION_NAME = "myfirstMDB"

FIELDS = {"first_name": True, "last_name": True, "dob": True, "_id": False}

with MongoClient(MONGODB_URI) as conn:
    collection = conn[DBS_NAME][COLLECTION_NAME]
    
    
    collection.insert({"first_name": "Ann", "last_name": "Person"})
    
    peeps = collection.find(projection=FIELDS)
    for doc in peeps:
        print(doc)