import flask

app = flask.Flask(__name__)

@app.route('/prueba', methods = ['POST'])
def hello_world():
    documento = {
            'data': 'Minha primeira API'
            }
    return flask.jsonify(documento)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
