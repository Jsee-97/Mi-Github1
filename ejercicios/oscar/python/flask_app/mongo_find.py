from pymongo import MongoClient


client = MongoClient()

collection = client.pessoa

res = collection.pessoa.find_one({'nome': 'Prueba'})

print(res)
