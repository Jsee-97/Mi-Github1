from pymongo import MongoClient


client = MongoClient()

collection = client.pessoa

documento = {
        'cpf': 7484054,
        'nome': 'Esther',
        'idade': 35,
            'UF': 'AM'
        }

collection.pessoa.insert_one(documento)

for documento in collection.pessoa.find():
    print(documento)
