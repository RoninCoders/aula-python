from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)

with open("teste.json") as file:
    data=file.read()

objeto = json.loads(data)

@app.route('/')
def hello_world():
    return "Minha primeira rota"

@app.route('/atividades', methods=['GET'])
def getAtividades():
    return jsonify(objeto)

@app.route('/criar', methods=['POST'])
def criarAtividade():
    return "Atividade criada"

@app.route('/atualizar', methods=['UPDATE'])
def updateAtividade():
    return "Atividade atualizada"

@app.route('/delete', methods=['DELETE'])
def deleteAtividade():
    return "Atividade deletada"


if __name__ == "__main__":
    app.run()
