from flask import Flask, render_template, request, Blueprint, jsonify
from flaskext.mysql import MySQL
import sqlite3
import os
import pycep_correios

from datetime import datetime
from controller.usuarioController import listar as service_listar, \
    localiza as service_localiza, \
    novo as service_novo, \
    atualiza as service_atualiza

usuarios_app = Blueprint('usuarios_app', __name__, template_folder='templates')


# def conectar():
#     return sqlite3.connect('tables/usuarios.db')

# Converte uma linha em um dicionário.
def row_to_dict(description, row):
    dict = {}
    for i in range(0, len(row)):
        dict[description[i][0]] = row[i]
    return dict

@usuarios_app.route("/logado", methods = ["POST"])
def validar_login():
    user = dict()
    user["documento"] = request.form["documento"].replace('.','').replace('-','')
    user["senha"] = request.form["senha"]
    #Validação temporária

    if(user["documento"] == '4321' and user["senha"]=='1234'):
        return render_template("cadastrar_produtos.html", mensagem = f"Seja bem vindo! tester")
    return render_template("index.html", mensagem = f"Documento e/ou senha invalidos")



# Converte uma lista de linhas em um lista de dicionários.
def rows_to_dict(description, rows):
    result = []
    for row in rows:
        result.append(row_to_dict(description, row))
    return result


# @usuarios_app.route("/novo_usuario", methods = ["GET"])
# def tela_cadastro_usuario():
#     return render_template("templates/cadastrar_usuarios.html")

@usuarios_app.route("/usuario", methods = ["POST"])
def cadastrar_usuarios():
    novo_usuario = dict()
    novo_usuario["nome"] = request.form["id_nome"]
    novo_usuario["telefone"] = request.form["id_telefone"]
    novo_usuario["email"] = request.form["id_email"]
    novo_usuario["documento"] = request.form["id_documento"]
    novo_usuario["cep"] = request.form["id_cep"]
    endereco = pycep_correios.get_address_from_cep(novo_usuario["cep"])
    novo_usuario["logradouro"] = endereco["logradouro"]
    novo_usuario["numero"] = request.form["id_numero"]
    novo_usuario["bairro"] = endereco["bairro"]
    novo_usuario["cidade"] = endereco["cidade"]
    novo_usuario["estado"] = devolve_nome_estado(endereco["uf"])
    novo_usuario["senha"] = request.form["id_senha"]
    novo_usuario["idCategoria"] = request.form["categoria"]
    new_user = novo_usuario["nome"]
    result = service_novo(novo_usuario)
    return render_template("index.html", mensagem = f"{new_user}, obrigado pelo cadastro")


@usuarios_app.route("/listar_usuario", methods = ["GET"])
def exibe_usuarios():
    lista = service_listar()
    return render_template("lista_usuarios.html", usuarios = lista)

@usuarios_app.route("/api_cep", methods = ["POST"])
def teste():
    cep = request.form['cep']
    try:
	    endereco = pycep_correios.get_address_from_cep(cep)
    except Exception as e:
	    jsonify({'Error': e.message})
    return jsonify(endereco)

@usuarios_app.route("/")
def menu():
    return render_template("index.html", mensagem = "")

#@usuarios_app.route("/cadastrar_usuarios")
#def usuarios_form():
#    return render_template("cadastrar_usuarios.html", editavel=None)

@usuarios_app.route("/usuario/<id_usuario>")
def rendireciona_update(id_usuario):
    localizado = service_localiza(id_usuario)
    return render_template("cadastrar_usuarios.html", editavel=localizado)

@usuarios_app.route("/usuario/<id_usu>", methods = ["POST"])
def editar_usuarios(id_usu):
    #ATUALIZAR PARA PEGAR APENAS OS DADOS DO PERFIL DAQUELE USUARIO
    edita_usuario = dict()
    edita_usuario["id"] = id_usu
    edita_usuario["nome"] = request.form["id_nome"]
    edita_usuario["telefone"] = request.form["id_telefone"]
    edita_usuario["email"] = request.form["id_email"]
    edita_usuario["documento"] = request.form["id_documento"]
    edita_usuario["cep"] = request.form["id_cep"]
    print(edita_usuario['cep'])
    endereco = pycep_correios.get_address_from_cep(edita_usuario['cep'])
    edita_usuario["logradouro"] = endereco["logradouro"]
    edita_usuario["numero"] = request.form["id_numero"]
    edita_usuario["bairro"] = endereco["bairro"]
    edita_usuario["cidade"] = endereco["cidade"]
    edita_usuario["estado"] = devolve_nome_estado(endereco["uf"])
    edita_usuario["senha"] = request.form["id_senha"]
    edita_usuario["idCategoria"] = request.form["categoria"]
    new_user = edita_usuario["nome"]
    result = service_atualiza(edita_usuario)
    return render_template("cadastrar_produtos.html", mensagem = f"{new_user}, usuario editado")

def devolve_nome_estado(uf):
    dados = [["SP", "SE", "São Paulo"], ["MG", "SE", "Minas Gerais"], ["RJ", "SE", "Rio de Janeiro"], ["BA", "NE", "Bahia"], ["RS", "S", "Rio Grande do Sul"], ["PR", "S", "Paraná"], ["PE", "NE", "Pernambuco"], ["CE", "NE", "Ceará"], ["PA", "N", "Pará"], ["MA", "NE", "Maranhão"], ["SC", "S", "Santa Catarina"], ["GO", "CO", "Goiás"], ["PB", "NE", "Paraíba"], ["ES", "SE", "Espírito Santo"], ["AM", "N", "Amazonas"], ["RN", "NE", "Rio Grande do Norte"], ["AL", "NE", "Alagoas"], ["PI", "NE", "Piauí"], ["MT", "CO", "Mato Grosso"], ["DF", "CO", "Distrito Federal"], ["MS", "CO", "Mato Grosso do Sul"], ["SE", "NE", "Sergipe"], ["RO", "N", "Rondônia"], ["TO", "N", "Tocantins"], ["AC", "N", "Acre"], ["AP", "N", "Amapá"], ["RR", "N", "Roraima"] ]
    for dado in dados:
        #0 == UF
        #01 == Regiao
        #02 == Estado
        if(uf == dado[0]):
            return dado[2]

