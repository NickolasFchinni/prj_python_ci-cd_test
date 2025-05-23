from flask import Flask, request, jsonify
from validator import validar_dados

app = Flask(__name__)

@app.route('/', methods=['GET'])
def server_rodando():
  return jsonify({"status": "sucesso", "mensagem": "Server rodando"}), 200

@app.route('/validar', methods=['POST'])
def validar():
  dados = request.get_json()

  resultado, erro = validar_dados(dados)

  if resultado:
    return jsonify({"status": "sucesso", "mensagem": "Dados válidos."}), 200
  else:
    return jsonify({"status": "erro", "mensagem": erro}), 400
  
if __name__ == '__main__':
  app.run(debug=True)