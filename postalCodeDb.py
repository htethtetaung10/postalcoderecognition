import pymongo
import json
from pymongo import InsertOne

# Mongo db connection
conn = pymongo.MongoClient()
conn.drop_database('postal_code')
db = conn['postal_code']
coll = db['postal_code_details']

documents = []

# Read json file
with open("postalCode.json", "r") as f:
    for document in f:
        doc = json.loads(document)
        documents.append(InsertOne(doc))
        # print(doc)
    f.close()
coll.bulk_write(documents)
conn.close()