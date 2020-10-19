import flask
import pymongo

app = flask.Flask(__name__)

client = pymongo.MongoClient()

collection = client.pessoa

@app.route('/', methods = ['POST'])
def hello_world():
    documento = {
            'data': 'Minha primeira API'
            }
    return flask.jsonify(documento)

@app.route('/prueba', methods = ['POST'])
def get_all_documents():
    documentos = [
            {
                'id': str(d.get('_id')),
                'nome': d.get('nome'),
                'idade': d.get('idade'),
                'UF': d.get('UF')

            } for d in collection.pessoa.find()
        ]
    return flask.jsonify(documentos)


@app.route('/delete/<nome>', methods = ['DELETE'])
def delete_by_name(nome):
    collection.pessoa.delete_one({
        'nome' : str(nome)
    })
    return flask.jsonify({'message': 'registro eliminado'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
