import flask
import pymongo

app = flask.Flask(__name__)

client = pymongo.MongoClient()

collection = client.pessoa

@app.route('/', methods = ['GET'])
def hello_world():
    documento = {
            'data': 'Minha primeira API'
            }
    return flask.jsonify(documento)

@app.route('/prueba', methods = ['GET'])
def get_all_documents():
    documentos = [
            {
                'id': str(d.get('_id')),
                'TS': d.get('TS'),
                'D': d.get('D'),
                'strength': d.get('strength'),
                'mac': d.get('mac'),
                'hostname': d.get('hostname')

            } for d in collection.pessoa.find()
        ]
    return flask.jsonify(documentos)


@app.route('/delete/<nome>', methods = ['DELETE'])
def delete_by_name(nome):
    collection.pessoa.delete_one({
        'nome' : str(nome)
    })
    return flask.jsonify({'message': 'registro eliminado'})

@app.route('/wifi/insert', methods = ['POST'])
def insert_wifi():
    doc = flask.request.json
    collection.pessoa.insert(doc)

    return flask.jsonify({'mensagem': 'Ingresado com sucesso'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
