from flask import Flask, render_template, request, Blueprint, jsonify

estoque_app = Blueprint('estoque_app', __name__, template_folder='templates')

from controller.produtosController import listar as service_listar_produto
from controller.estoqueController import localiza_compras, listar as service_listar, \
    localiza as service_localiza, \
    novo as service_novo


@estoque_app.route("/estoque", methods = ["POST"])
def cadastra_estoque():
    estoque = dict()
    estoque["id_produto"] = request.form["produto"]
    for p in service_listar_produto():
        if str(p.id) == estoque["id_produto"]:
            estoque["nome"] = p.nome
            estoque["cor"] = p.cor
            estoque["unidade"] = p.unidade
            break
    
    estoque["tipo"]=request.form["id_tipo_produto"]
    estoque["estoque"]=request.form["id_qtd_produto"]
    estoque["preco"]=request.form["id_preco_produto"]
    service_novo(estoque)
    localizado=localiza_compras()
    return render_template("home.html", mensagem="Estoque cadastrado com sucesso", estoque=localizado, editavel=None)


@estoque_app.route("/estoque")
def visualiza_estoque():
    localizado = service_listar_produto()
    return render_template("cadastrar_estoque.html", mensagem="", editavel=None,produtos=localizado)

@estoque_app.route("/estoque_lista")
def carrega_estoque():
    localizado=service_listar();
    return render_template("lista_estoque.html", mensagem="", editavel=None, estoque=localizado)
