import pymongo
client = pymongo.MongoClient("mongodb+srv://santosh:<password>@cluster0.awz3j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {"key":"value"}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)