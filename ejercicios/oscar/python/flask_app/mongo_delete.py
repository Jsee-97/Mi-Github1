from pymongo import MongoClient


client = MongoClient()

collection = client.pessoa

collection.pessoa.delete_one({'idade': 44})

for item in collection.pessoa.find():
    print(item)
