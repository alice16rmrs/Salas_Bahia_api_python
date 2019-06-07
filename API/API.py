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
        'preco': 1200.00
    },
    {
        'id': 2,
        'nome': u'Microondas',
        'preco': 650.00
    },
    {
        'id': 3,
        'nome': u'Coqueteleira',
        'preco':120.00
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
        'preco': request.json.get('preco', "")
    }
    # Validação
    if len(produto) == 0:
        abort(404)
    if 'nome' in request.json and type(request.json['nome']) is not str:
        abort(400)
    if 'preco' in request.json and type(request.json['preco']) is not float:
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
    if 'preco' in request.json and type(request.json['preco']) is not float:
        abort(400)
    #
    produto[0]['nome'] = request.json.get('nome', produto[0]['nome'])
    produto[0]['preco'] = request.json.get('preco', produto[0]['preco'])
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
