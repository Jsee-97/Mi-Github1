from pymongo import MongoClient


client = MongoClient()

collection = client.pessoa

collection.pessoa.update_one({'nome': 'Prueba'},
                            {'$set': {'UF': 'PE'}})

res = collection.pessoa.find_one({'nome':'Prueba'})
        
print(res)
