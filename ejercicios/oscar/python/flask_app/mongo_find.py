from pymongo import MongoClient


client = MongoClient()

collection = client.pessoa
count = 0

for x in collection.pessoa.find({'TS': '1603141937'}):
    count += 1
    print(x, "\n")

print('Tem', count, 'Dispositivos')
