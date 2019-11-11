import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
print(myclient.list_database_names())

with myclient:
    db = myclient.user
    print(db.collection_names())