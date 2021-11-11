from flask import Flask, render_template, request, Blueprint, jsonify
import os
import sqlite3

produtos_app = Blueprint('produtos_app', __name__, template_folder='templates')

from datetime import datetime
from controller.produtosController import listar as service_listar, \
    localiza as service_localiza, \
    novo as service_novo, \
    atualiza as service_atualiza

from controller.usuarioController import listar as service_usuario_listar, localiza as service_usuario_localiza
from controller.carrinhoController import novo as novo_carrinho, listar as listar_carrinho


from API_TOMTOM import TOMTOM
__tomtom = TOMTOM()


@produtos_app.route("/produtos_lista")
def lista_produto():
    listados = list()
    produtos = service_listar()
    local_user = service_usuario_localiza(os.environ['__usuario_id'])
    usuarios = service_usuario_listar()
    for produto in produtos:
        for usu in usuarios:
            #Criar um espaço para os itens daquele fornecedor
            if(usu.id != local_user.id and usu.id == produto.id_fornecedor):
                produto.km = __tomtom.resolve_distancia(local_user, usu)
                listados.append(produto)
    return render_template("lista_produtos.html", produtos=bubble_sort(listados))

@produtos_app.route("/produto")
def form_prod():
    return render_template("cadastrar_produtos.html", editavel="")

@produtos_app.route("/produtos", methods = ["POST"])
def cadastrar_produtos():
    novo_produto = dict()
    novo_produto["id_fornecedor"] = os.environ['__usuario_id']
    novo_produto["nome"] = request.form["id_nome_produto"]
    novo_produto["descricao"] = request.form["id_descricao"]
    novo_produto["quantidade"] = request.form["id_qtd_produto"]
    novo_produto["preco"] = request.form["id_preco_produto"]
    novo_produto["status"] = "Disponivel"
    # print(novo_produto)
    new_user = novo_produto["nome"]
    result = service_novo(novo_produto)
    return render_template("cadastrar_produtos.html", mensagem = "Produto "+f"{new_user}, cadastrado com sucesso")


def bubble_sort(lista):
    #KM DE VANTAGEM
     elementos = len(lista)-1
     ordenado = False
     while not ordenado:
         ordenado = True
         for i in range(elementos):
             if lista[i].km > lista[i+1].km:
                 lista[i], lista[i+1] = lista[i+1],lista[i]
                 ordenado = False     
     return lista