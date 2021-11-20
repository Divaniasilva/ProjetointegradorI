from flask import Flask, render_template, request, Blueprint, jsonify
import mysql.connector as MySQL

estoque_app = Blueprint('estoque_app', __name__, template_folder='templates')

from datetime import datetime
from controller.produtosController import listar as service_listar_produto
from controller.estoqueController import listar as service_listar, \
    localiza as service_localiza, \
    novo as service_novo


#from controller.usuarioController import listar as service_usuario_listar, localiza as service_usuario_localiza
#from controller.carrinhoController import novo as novo_carrinho, listar as listar_carrinho


# @produtos_app.route("/produtos_lista")
# def lista_produto():
#     listados = list()
#     produtos = service_listar()
#     local_user = service_usuario_localiza(os.environ['__usuario_id'])
#     usuarios = service_usuario_listar()
#     for produto in produtos:
#         for usu in usuarios:
#             #Criar um espaço para os itens daquele fornecedor
#             if(usu.id != local_user.id and usu.id == produto.id_fornecedor):
#                 #produto.km = __tomtom.resolve_distancia(local_user, usu)
#                 listados.append(produto)
#     return render_template("lista_produtos.html", produtos=bubble_sort(listados))

# @estoque_app.route("/produtos_lista")
# def lista_produto():
#     listados = list()
#     produtos = service_listar()
#     for produto in produtos:
#        listados.append(produto)
#     return render_template("lista_produtos.html", produtos=listados)

@estoque_app.route("/estoque")
def validar_login():
    localizado = service_listar_produto()
    return render_template("cadastrar_estoque.html", mensagem="", editavel=None,produtos=localizado)

@estoque_app.route("/estoque_lista")
def carrega_estoque():
    localizado=service_listar();
    return render_template("lista_estoque.html", mensagem="", editavel=None, estoque=localizado)

# @estoque_app.route("/produtos", methods = ["POST"])
# def cadastrar_produtos():
#     novo_produto = dict()
#     novo_produto["nome"] = request.form["id_nome_produto"]
#     novo_produto["cor"] = request.form["id_cor"]
#     novo_produto["unidade"] = request.form["id_unidade"]
#     # print(novo_produto)
#     new_user = novo_produto["nome"]
#     print(novo_produto)
#     result = service_novo(novo_produto)
#     return render_template("cadastrar_produtos.html", mensagem = "Produto "+f"{new_user}, cadastrado com sucesso", editavel=None)

# @estoque_app.route("/produtos/<id_produto>")
# def rendireciona_update(id_produto):
#     localizado = service_localiza(id_produto)
#     return render_template("cadastrar_produtos.html", editavel=localizado)

# @estoque_app.route("/produtos/<id_prod>", methods = ["POST"])
# def editar_usuarios(id_prod):
#     #ATUALIZAR PARA PEGAR APENAS OS DADOS DO PERFIL DAQUELE USUARIO
#     edita_produto = dict()
#     edita_produto["id"] = id_prod
#     edita_produto["nome"] = request.form["id_nome_produto"]
#     edita_produto["cor"] = request.form["id_cor"]
#     edita_produto["unidade"] = request.form["id_unidade"]
#     new_user = edita_produto["nome"];
#     print('foi 1')
#     service_atualiza(edita_produto)
#     return render_template("cadastrar_produtos.html", mensagem = f"{new_user}, produto base editado", editavel=None)
