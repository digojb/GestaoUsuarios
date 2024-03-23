from flask import Blueprint, render_template, request
from Database.Models.cliente import Cliente

cliente_route = Blueprint('cliente', __name__)

"""
Rota de Clientes
    - /clientes/ (GET) - Listar os cliente
    - /clientes/ (POST) - Inserir o cliente no servidor
    - /clientes/new (GET) - Renderizar o formulario para criar um cliente
    - /clientes/<id> (GET) - Obter os dados de um cliente
    - /clientes/<id>/edit (GET) - Renderizar um formulario para editar um cliente 
    - /clientes/<id>/update (PUT) - Atualizar os dados do cliente
    - /clientes/<id>/delete (DELETE) - Deleta o registro do usuaro
"""

#Rotas: 
@cliente_route.route('/')
def lista_clientes():
    """ Listar os cliente """

    clientes = Cliente.select()

    return render_template('lista_clientes.html', clientes = clientes)


@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    """ Inserir o cliente no servidor """

    data = request.json

    novo_usuario = Cliente.create(
        nome = data['nome'],
        email = data['email'],
    )

    return render_template('item_cliente.html', cliente=novo_usuario)


@cliente_route.route('/new')
def form_cliente():
    """ Renderizar o formulario para criar um cliente """
    
    return render_template('form_cliente.html')


@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    """ Obter os dados de um cliente """

    cliente = Cliente.get_by_id(cliente_id)

    return render_template('detalhe_cliente.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    """ Renderizar um formulario para editar um cliente  """

    cliente = Cliente.get_by_id(cliente_id)

    return render_template('form_cliente.html', cliente = cliente)


@cliente_route.route('/<int:cliente_id>/update', methods = ['PUT'])
def atualizar_cliente(cliente_id):
    """ Atualizar os dados do cliente """
    
    #obter dados do formulario de edição
    data = request.json

    cliente_editado = Cliente.get_by_id(cliente_id)
    cliente_editado.nome = data['nome']
    cliente_editado.email = data['email']
    cliente_editado.save()

    return render_template('item_cliente.html', cliente = cliente_editado)   
      

@cliente_route.route('/<int:cliente_id>/delete', methods = ['DELETE'])
def deletar_cliente(cliente_id):
    """ Deleta o registro do usuaro """

    cliente = Cliente.get_by_id(cliente_id)
    cliente.delete_instance()

    return {'deleted': 'ok'}
