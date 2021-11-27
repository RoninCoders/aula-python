from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Minha primeira rota"

@app.route('/atividades', methods=['GET'])
def getAtividades():
    return "Todas as atividades"

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
