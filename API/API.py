from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import url_for


app = Flask(__name__)

# Produtos Default
produtos = [
    {
        'id': 1,
        'nome': u'Cama',
        'qtd': 1
    },
    {
        'id': 2,
        'nome': u'Microondas',
        'qtd': 3
    },
    {
        'id': 3,
        'nome': u'Coqueteleira',
        'qtd': 4
    }
]

## Make Public
def make_public_produto(produto):
    new_produto = {}
    for field in produto:
        if field == 'id':
            new_produto['uri'] = url_for('get_produto', produto_codigo=produto['id'], _external=True)
        else:
            new_produto[field] = produto[field]
    return new_produto


## Métodos GET
@app.route('/crud/api/produtos', methods=['GET'])
def get_produtos():
    return jsonify({'produtos': [make_public_produto(produto) for produto in produtos]})


@app.route('/crud/api/produtos/<int:produto_id>', methods=['GET'])
def get_produto(produto_id):
    produto = [produto for produto in produtos if produto['id'] == produto_id]
    if len(produto) == 0:
        abort(404)
    return jsonify({'produto': produto[0]})


## Método POST
@app.route('/crud/api/produtos', methods=['POST'])
def create_produto():
    produto = {
        'id': produtos[-1]['id'] + 1,
        'nome': request.json.get('nome', ""),
        'qtd': request.json.get('qtd', "")
    }
    # Validação
    if len(produto) == 0:
        abort(404)
    if 'nome' in request.json and type(request.json['nome']) is not str:
        abort(400)
    if 'qtd' in request.json and type(request.json['qtd']) is not int:
        abort(400)
    #
    produtos.append(produto)
    return jsonify({'produto': produto}), 201


## Método PUT
@app.route('/crud/api/produtos/<int:produto_id>', methods=['PUT'])
def update_produto(produto_id):
    produto = [produto for produto in produtos if produto['id'] == produto_id]
    # Validação
    if len(produto) == 0:
        abort(404)
    if 'nome' in request.json and type(request.json['nome']) is not str:
        abort(400)
    if 'qtd' in request.json and type(request.json['qtd']) is not int:
        abort(400)
    #
    produto[0]['nome'] = request.json.get('nome', produto[0]['nome'])
    produto[0]['qtd'] = request.json.get('qtd', produto[0]['qtd'])
    return jsonify({'produto': produto[0]})


## Método DELETE
@app.route('/crud/api/produtos/<int:produto_id>', methods=['DELETE'])
def delete_produto(produto_id):
    produto = [produto for produto in produtos if produto['id'] == produto_id]
    if len(produto) == 0:
        abort(404)
    produtos.remove(produto[0])
    return jsonify({'result': True})


## Erro
@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)


## MAIN
if __name__ == '__main__':
    app.run(debug=True)
