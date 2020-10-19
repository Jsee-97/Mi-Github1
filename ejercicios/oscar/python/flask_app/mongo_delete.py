from pymongo import MongoClient


client = MongoClient()

collection = client.pessoa

collection.pessoa.delete_one({'nome': 'Prueba'})

for item in collection.pessoa.find():
    print(item)
